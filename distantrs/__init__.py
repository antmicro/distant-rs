import grpc, uuid
import google.auth
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

RESULT_STORE_URL = "resultstore.googleapis.com"

def is_channel_operational(channel, timeout=3):
    try:
        grpc.channel_ready_future(channel).result(timeout=timeout)
        return True
    except grpc.FutureTimeoutError:
        return False

def get_grpcs_channel():
    credentials, _ = google.auth.default()
    http_request = google.auth.transport.requests.Request()
    channel = google.auth.transport.grpc.secure_authorized_channel(
            credentials, http_request, RESULT_STORE_URL)

    if not is_channel_operational(channel):
        raise ConnectionError("gRPC connection failed.")

    return channel

def get_invocation(uuid):
    channel = get_grpcs_channel()
    fields = []

    for f in inv.Invocation().DESCRIPTOR.fields_by_name:
        fields.append(f)

    fieldmask = [('X-Goog-FieldMask'.lower(), ",".join(fields))]

    stub = rs_grpc.ResultStoreDownloadStub(channel)

    request = rs.GetInvocationRequest(name=f'invocations/{uuid}')

    return stub.GetInvocation(request=request, metadata=fieldmask)

