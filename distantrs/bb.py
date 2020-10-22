import requests, shutil, posixpath
from tempfile import mkdtemp
from distantrs import Invocation
from urllib.parse import urlparse
from distantrs.proto.proto import (
        invocation_pb2 as iv, 
        build_event_stream_pb2 as bes
        )

NOTFOUND = b'record not found\n'

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

    for ev in bb_i.event:
        b_ev = ev.build_event
        b_id = b_ev.id.WhichOneof('id')

        close_update_duration = True

        if b_id == 'build_tool_logs':
            for b_ev_log in b_ev.build_tool_logs.log:
                if b_ev_log.name == 'elapsed time':
                    duration = int(b_ev_log.contents.decode())
                    i.update_duration(duration)
                    close_update_duration = False
                    break

    i.close(update_duration=close_update_duration)

    return i.invocation_id
