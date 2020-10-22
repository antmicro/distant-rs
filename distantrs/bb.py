import requests, shutil, posixpath, os
from hashlib import sha256
from tempfile import mkdtemp
from distantrs import Invocation
from urllib.parse import urlparse, urlencode
from distantrs.proto.proto import (
        invocation_pb2 as iv, 
        build_event_stream_pb2 as bes
        )

NOTFOUND = b'record not found\n'

def download_file(url, dl_path):
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return dl_path

def get_file_from_cas(invocation_url, bytestream_uri, dl_path):
    u = urlparse(invocation_url)
    suffix = "/".join(list(filter(None, u.path.split("/")[:-2])))
    params = {'filename':os.path.basename(dl_path), 'bytestream_url':bytestream_uri}
    f_endpoint = 'file/download?' + urlencode(params)

    if suffix:
        path = [u.netloc, suffix, f_endpoint]
    else:
        path = [u.netloc, f_endpoint]

    f_url = "{}://{}".format(u.scheme, "/".join(path))

    return download_file(f_url, dl_path)

def get_bb_invocation(url):
    u = urlparse(url)
    suffix = "/".join(list(filter(None, u.path.split("/")[:-2])))
    rpc_endpoint = 'rpc/BuildBuddyService/GetInvocation'

    if suffix:
        path = [u.netloc, suffix, rpc_endpoint]
    else:
        path = [u.netloc, rpc_endpoint]

    rpc_url = "{}://{}".format(u.scheme, "/".join(path))

    ivr = iv.GetInvocationRequest()
    ivr.lookup.invocation_id = url.split("/")[-1]

    r = requests.post(rpc_url, data=ivr.SerializeToString(), headers={"Content-Type":"application/proto"})

    if r.content == NOTFOUND:
        raise Exception(NOTFOUND.decode())

    ivresp = iv.GetInvocationResponse()
    ivresp.MergeFromString(r.content)

    return ivresp.invocation[0]

def upload_invocation(url, mirror_iid=False, **kwargs):
    bb_i = get_bb_invocation(url)

    if mirror_iid:
        iid = bb_i.invocation_id
    else:
        iid = None

    i = Invocation(
            **kwargs, 
            invocation_id=iid,
            user=bb_i.user, 
            hostname=bb_i.host
            )
    i.open()

    temp_dir = mkdtemp()
    main_log = posixpath.join(temp_dir, 'build.log')

    with open(main_log, 'w') as log_fh:
        log_fh.write(bb_i.console_buffer)

    i.send_file('build.log', main_log)

    if bb_i.success:
        i.update_status(5)
    else:
        i.update_status(6)

    targets = {}

    for ev in bb_i.event:
        b_ev = ev.build_event
        b_id = b_ev.id.WhichOneof('id')

        close_update_duration = True

        if b_id == 'build_tool_logs':
            for b_ev_log in b_ev.build_tool_logs.log:
                if b_ev_log.name == 'elapsed time':
                    duration = int(float(b_ev_log.contents.decode()))
                    i.update_duration(duration)
                    close_update_duration = False
                    break
        elif b_id == 'target_configured':
            target_name = b_ev.id.target_configured.label.replace(" ", "_")
            targets[target_name] = {
                    'name':target_name,
                    'log':'',
                    'success':False,
                    'files':[],
                    'seconds':0,
                    }
        elif b_id == 'target_completed':
            target_name = b_ev.id.target_completed.label.replace(" ", "_")
            targets[target_name]['success'] = b_ev.completed.success
            targets[target_name]['files'] = b_ev.completed.important_output
        elif b_id == 'test_summary':
            target_name = b_ev.id.test_summary.label.replace(" ", "_")
            for b_ev_passed in b_ev.test_summary.passed:
                if b_ev_passed.name == 'test.log':
                    targets[target_name]['log'] = b_ev_passed.uri
                    break
            targets[target_name]['seconds'] = b_ev.test_summary.total_run_duration_millis // 1000

    for t in targets.values():
        hashed_target_name = sha256(t['name'].encode('utf-8')).hexdigest()[:10]
        i.announce_target(t['name'])

        if t['log']:
            test_log_path = posixpath.join(temp_dir, f'test-{hashed_target_name}.log')
            get_file_from_cas(
                    invocation_url=url,
                    bytestream_uri=t['log'],
                    dl_path=test_log_path,
                    )
            i.add_log_to_target(t['name'], test_log_path)

        i.finalize_target(
                name=t['name'],
                success=t['success'],
                seconds=t['seconds'],
                )

        print(t)

    i.close(update_duration=close_update_duration)

    return f'https://source.cloud.google.com/results/invocations/{i.invocation_id}'
