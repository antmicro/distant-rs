import grpc, sys
import google.auth.transport.grpc
import google.auth.transport.requests
from distantrs.proto.google.devtools.resultstore.v2 import (
        resultstore_download_pb2 as rs,
        resultstore_download_pb2_grpc as rs_grpc
        )
from google import auth as google_auth

def check(chan):
    try:
        grpc.channel_ready_future(chan).result(timeout=3)
        return True
    except grpc.FutureTimeoutError:
        return False

credentials, _ = google_auth.default()
http_request = google.auth.transport.requests.Request()

ch = google.auth.transport.grpc.secure_authorized_channel(
        credentials, http_request, "resultstore.googleapis.com")

stub = rs_grpc.ResultStoreDownloadStub(ch)

fieldmask = [('X-Goog-FieldMask'.lower(), 'name,id,status_attributes,timing,invocation_attributes,workspace_info,properties,files,coverage_summaries,aggregate_coverage,file_processing_errors')]


if __name__ == '__main__':
    try:
        iid = sys.argv[1]
    except:
        sys.exit(1)

    r = rs.GetInvocationRequest(name=f"invocations/{iid}")

    invocation = stub.GetInvocation(request=r, metadata=fieldmask)

    print(invocation)
