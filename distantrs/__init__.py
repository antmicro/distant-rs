import grpc, uuid, platform, datetime, requests, os
import google.auth
import google.auth.transport.grpc
import google.auth.transport.requests
from google.cloud import storage
from distantrs.proto.google.devtools.resultstore.v2 import (
        resultstore_download_pb2 as rs,
        resultstore_download_pb2_grpc as rs_grpc,
        resultstore_upload_pb2 as rsu,
        resultstore_upload_pb2_grpc as rsu_grpc,
        invocation_pb2 as inv,
        invocation_pb2_grpc as inv_grpc,
        file_pb2 as inv_f,
        file_pb2_grpc as inv_f_grpc,
        )
from google.protobuf import (
        timestamp_pb2 as ts,
        field_mask_pb2 as fm,
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

def infer_project_id():
    r = requests.get(
            'http://metadata.google.internal/computeMetadata/v1/project/numeric-project-id',
            headers={'Metadata-Flavor':'Google'},
            )
    r.raise_for_status()
    return r.text

def get_invocation(uuid):
    channel = get_grpcs_channel()
    fields = []

    for f in inv.Invocation().DESCRIPTOR.fields_by_name:
        fields.append(f)

    fieldmask = [('X-Goog-FieldMask'.lower(), ",".join(fields))]

    stub = rs_grpc.ResultStoreDownloadStub(channel)

    request = rs.GetInvocationRequest(name=f'invocations/{uuid}')

    return stub.GetInvocation(request=request, metadata=fieldmask)

class Invocation:
    def __init__(
            self, 
            project_id=None,
            bucket_name=None,
            invocation_id=None, 
            auth_token=None
            ):
        self.channel = get_grpcs_channel()
        self.invocation_id = invocation_id or str(uuid.uuid4())
        self.auth_token = auth_token or str(uuid.uuid4())
        self.stub = rsu_grpc.ResultStoreUploadStub(self.channel)

        self.project_id = project_id or infer_project_id()

        self.bucket_name = bucket_name or os.environ['DISTANT_RS_BUCKET']
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(self.bucket_name)

        self.user = 'distant-rs'
        self.hostname = platform.node()

        self.invocation_proto = None

    def __minimal_invocation(self):
        i = inv.Invocation()
        i.id.invocation_id = self.invocation_id
        i.name = f'invocations/{self.invocation_id}'
        return i

    def merge(self, invocation):
        fieldmask = fm.FieldMask()
        for f in invocation.ListFields():
            fieldmask.paths.append(f[0].name)

        mir = rsu.MergeInvocationRequest(
                request_id=str(uuid.uuid4()),
                invocation=invocation,
                update_mask=fieldmask,
                authorization_token=self.auth_token,
                )
        return self.stub.MergeInvocation(mir)

    def update_status(self, code):
        i = self.__minimal_invocation()
        i.status_attributes.status = code
        return self.merge(i)

    def send_file(self, name, path):
        blob_path = f'{self.invocation_id}/{name}'
        gs_path = f'gs://{self.bucket_name}/{blob_path}'

        blob = self.bucket.blob(blob_path)
        blob.upload_from_filename(path)

        f_proto = inv_f.File(
                uid=str(uuid.uuid4()),
                uri=gs_path
                )

        i = self.__minimal_invocation()
        i.files.append(f_proto)
        self.merge(i)
        
        
    def open(self, timeout=30):
        i = inv.Invocation()
        i.id.invocation_id = self.invocation_id
        i.name = f'invocations/{self.invocation_id}'

        i.status_attributes.status = 1

        i.timing.start_time.GetCurrentTime()

        i.invocation_attributes.project_id = self.project_id
        i.invocation_attributes.users.append(self.user)
        i.invocation_attributes.labels.append('distant-rs')

        i.workspace_info.hostname = self.hostname

        t = ts.Timestamp()
        t.FromDatetime(datetime.datetime.now() + datetime.timedelta(minutes=timeout))

        cir = rsu.CreateInvocationRequest(
                request_id=str(uuid.uuid4()),
                invocation_id=self.invocation_id,
                invocation=i,
                authorization_token=self.auth_token,
                auto_finalize_time=t,
                )

        cir_request = self.stub.CreateInvocation(cir)
        self.invocation_proto = i
        return cir_request

    def close(self):
        fin = rsu.FinalizeInvocationRequest(
                name=f'invocations/{self.invocation_id}',
                authorization_token=self.auth_token
                )
        return self.stub.FinalizeInvocation(fin)

