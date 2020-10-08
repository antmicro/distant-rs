import grpc, sys, uuid
import google.auth.transport.grpc
import google.auth.transport.requests
from distantrs.proto.google.devtools.resultstore.v2 import (
        resultstore_download_pb2 as rs,
        resultstore_download_pb2_grpc as rs_grpc,
        resultstore_upload_pb2 as rsu,
        resultstore_upload_pb2_grpc as rsu_grpc,
        invocation_pb2 as inv,
        invocation_pb2_grpc as inv_grpc,
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

stub = rsu_grpc.ResultStoreUploadStub(ch)

fieldmask = [('X-Goog-FieldMask'.lower(), 'name,id,status_attributes,timing,invocation_attributes,workspace_info,properties,files,coverage_summaries,aggregate_coverage,file_processing_errors')]

with open("template_invocation.pb2", "rb") as f:
    t_inv = f.read()

invocation_id = str(uuid.uuid4())

inject_invocation = inv.Invocation()
inject_invocation.ParseFromString(t_inv)
inject_invocation.id.invocation_id = invocation_id
assert inject_invocation.properties[0].key == "BAZEL_BUILD_ID"
inject_invocation.properties[0].value = invocation_id
inject_invocation.workspace_info.hostname = "very-cool-hostname"
inject_invocation.files.pop(1)
inject_invocation.timing.duration.seconds = 10
inject_invocation.timing.duration.nanos = 239000000

inject_invocation.status_attributes.status = 1

cir = rsu.CreateInvocationRequest()
cir.request_id = str(uuid.uuid4())
cir.invocation_id = invocation_id
cir.invocation.CopyFrom(inject_invocation)
cir.authorization_token = str(uuid.uuid4())

fin = rsu.FinalizeInvocationRequest()
fin.name = f'invocations/{invocation_id}'
fin.authorization_token = cir.authorization_token

if __name__ == '__main__':
    creat = stub.CreateInvocation(request=cir)
    print(creat)
    final = stub.FinalizeInvocation(request=fin)
    print(final)
