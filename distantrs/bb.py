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
    rpc_url = "{}://{}".format(
            u.scheme, 
            "/".join([u.netloc,suffix,'rpc/BuildBuddyService/GetInvocation'])
            )

    ivr = iv.GetInvocationRequest()
    ivr.lookup.invocation_id = url.split("/")[-1]

    r = requests.post(rpc_url, data=ivr.SerializeToString())

    if r.content == NOTFOUND:
        raise Exception(NOTFOUND.decode())

    ivresp = iv.GetInvocationResponse()
    ivresp.MergeFromString(r.content)

    return ivresp.invocation[0]

def upload_invocation(url, **kwargs):
    bb_i = get_bb_invocation(url)

    i = Invocation(**kwargs, user=bb_i.user, hostname=bb_i.host)
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

    i.close()

    return i.invocation_id
