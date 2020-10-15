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
        file_pb2 as inv_f,
        target_pb2 as tgt,
        configured_target_pb2 as ctgt,
        configuration_pb2 as inv_conf,
        action_pb2 as inv_act,
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
    credentials, _ = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
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
        self.invocation_path = f'invocations/{self.invocation_id}'
        self.auth_token = auth_token or str(uuid.uuid4())
        self.stub = rsu_grpc.ResultStoreUploadStub(self.channel)

        self.project_id = project_id or infer_project_id()

        self.bucket_name = bucket_name or os.environ['DISTANT_RS_BUCKET']
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(self.bucket_name)

        self.user = 'distant-rs'
        self.hostname = platform.node()

        self.targets = {}

        self.invocation_proto = None

    def __minimal_invocation(self):
        i = inv.Invocation()
        i.id.invocation_id = self.invocation_id
        i.name = self.invocation_path
        return i

    def merge(self, invocation, fieldmask_list=None):
        fieldmask = fm.FieldMask()

        if fieldmask_list is None:
            for f in invocation.ListFields():
                fieldmask.paths.append(f[0].name)
        else:
            fieldmask.paths.MergeFrom(fieldmask_list)

        mir = rsu.MergeInvocationRequest(
                request_id=str(uuid.uuid4()),
                invocation=invocation,
                update_mask=fieldmask,
                authorization_token=self.auth_token,
                )
        mir_request = self.stub.MergeInvocation(mir)
        self.invocation_proto.MergeFrom(invocation)
        return mir_request

    def update_status(self, code):
        i = self.__minimal_invocation()
        i.status_attributes.status = code
        return self.merge(i)

    def update_duration(self, seconds=None):
        i = self.__minimal_invocation()
        i.timing.CopyFrom(self.invocation_proto.timing)

        if seconds is None:
            i.timing.duration.FromTimedelta(
                    datetime.datetime.now() - i.timing.start_time.ToDatetime())
        else:
            i.timing.duration.FromSeconds(seconds)

        return self.merge(i)

    def __upload_file_gen_proto(self, name, path, uid=None):
        blob_path = f'{self.invocation_id}/{name}'
        gs_path = f'gs://{self.bucket_name}/{blob_path}'

        blob = self.bucket.blob(blob_path)
        blob.upload_from_filename(path)

        if uid is None:
            uid = str(uuid.uuid4())

        f_proto = inv_f.File(
                uid=uid,
                uri=gs_path,
                )
        f_proto.length.value = os.path.getsize(path)

        return f_proto

    def send_configuration(self, conf_name="default"):
        c = inv_conf.Configuration(
                name=f'{self.invocation_path}/configs/{conf_name}'
                )
        c.id.invocation_id = self.invocation_id
        c.id.configuration_id = conf_name
        c.configuration_attributes.cpu = 'k8'

        ccr = rsu.CreateConfigurationRequest(
                request_id=str(uuid.uuid4()),
                parent=self.invocation_path,
                config_id=conf_name,
                configuration=c,
                authorization_token=self.auth_token,
                )
        ccr_request = self.stub.CreateConfiguration(ccr)
        return ccr_request

    def send_file(self, name, path):
        f_proto = self.__upload_file_gen_proto(name, path)
        i = self.__minimal_invocation()
        i.files.append(f_proto)
        return self.merge(i)

    def send_file_target(self, target_name, file_name, file_path):
        f_proto = self.__upload_file_gen_proto(f'{target_name}/{file_name}', file_path)
        fieldmask = fm.FieldMask()
        fieldmask.paths.MergeFrom(['files'])

        a = self.targets[target_name][2]
        a.files.append(f_proto)

        mar = rsu.MergeActionRequest(
                request_id=str(uuid.uuid4()),
                action=a,
                update_mask=fieldmask,
                authorization_token=self.auth_token,
                create_if_not_found=False
                )
        mar_request = self.stub.MergeAction(mar)
        self.targets[target_name][2] = a

        return mar_request

    def add_log_to_target(self, target_name, log_path):
        f_proto = self.__upload_file_gen_proto(
                f'{target_name}/test.log', 
                log_path,
                uid='test.log'
                )

        ct = self.targets[target_name][1]

        action_id = 'test_log_action'
        conf_id = 'default'
        
        a = inv_act.Action()
        a.name = f'{ct.name}/actions/{action_id}'
        a.id.invocation_id = self.invocation_id
        a.id.target_id = target_name
        a.id.configuration_id = conf_id
        a.id.action_id = action_id
        a.status_attributes.status = 1
        a.test_action.SetInParent()
        a.files.append(f_proto)

        car = rsu.CreateActionRequest(
                request_id=str(uuid.uuid4()),
                parent=ct.name,
                action_id=action_id,
                action=a,
                authorization_token=self.auth_token
                )

        car_request = self.stub.CreateAction(car)

    def announce_target(self, name):
        t = tgt.Target()
        t.id.invocation_id = self.invocation_id
        t.id.target_id = name
        t.name = f'invocations/{self.invocation_id}/targets/{name}'
        t.status_attributes.status = 1
        t.timing.start_time.GetCurrentTime()
        t.target_attributes.type = 2
        t.visible = True

        ctr = rsu.CreateTargetRequest(
                request_id=str(uuid.uuid4()),
                parent=self.invocation_path,
                target_id=name,
                authorization_token=self.auth_token,
                target=t,
                )

        ctr_request = self.stub.CreateTarget(ctr)

        conf_id = 'default'

        ct = ctgt.ConfiguredTarget()
        ct.name = f'{self.invocation_path}/targets/{name}/configuredTargets/{conf_id}'
        ct.id.invocation_id = self.invocation_id
        ct.id.target_id = name
        ct.id.configuration_id = conf_id
        ct.status_attributes.status = 1
        ct.timing.CopyFrom(t.timing)

        cctr = rsu.CreateConfiguredTargetRequest(
                request_id=str(uuid.uuid4()),
                parent=t.name,
                config_id=conf_id,
                configured_target=ct,
                authorization_token=self.auth_token
                )
        cctr_request = self.stub.CreateConfiguredTarget(cctr)

        action_id = 'build'
        a = inv_act.Action()
        a.name = f'{ct.name}/actions/{action_id}'
        a.id.invocation_id = self.invocation_id
        a.id.target_id = name
        a.id.configuration_id = conf_id
        a.id.action_id = action_id
        a.status_attributes.status = 1
        a.timing.CopyFrom(t.timing)
        a.build_action.SetInParent()

        car = rsu.CreateActionRequest(
                request_id=str(uuid.uuid4()),
                parent=ct.name,
                action_id=action_id,
                action=a,
                authorization_token=self.auth_token
                )

        car_request = self.stub.CreateAction(car)

        self.targets[name] = [t, ct, a]

        return ctr_request, cctr_request, car_request

    def finalize_target(self, name, success):
        fieldmask = fm.FieldMask()
        fieldmask.paths.MergeFrom(['timing.duration', 'status_attributes.status'])

        t = self.targets[name][0]
        ct = self.targets[name][1]

        # Taken from the Status enum in common.proto
        if success:
            status_int = 5
        else:
            status_int = 6

        t.status_attributes.status = status_int
        ct.status_attributes.CopyFrom(t.status_attributes)

        t.timing.duration.FromTimedelta(
                datetime.datetime.now() - t.timing.start_time.ToDatetime())
        ct.timing.CopyFrom(t.timing)

        mtr = rsu.MergeTargetRequest(
                target=t,
                update_mask=fieldmask,
                authorization_token=self.auth_token,
                create_if_not_found=False
                )
        mtr_request = self.stub.MergeTarget(mtr)

        mctr = rsu.MergeConfiguredTargetRequest(
                request_id=str(uuid.uuid4()),
                configured_target=ct,
                update_mask=fieldmask,
                authorization_token=self.auth_token,
                create_if_not_found=False
                )

        mctr_request = self.stub.MergeConfiguredTarget(mctr)

        self.targets[name][0] = t
        self.targets[name][1] = ct

        fctr = rsu.FinalizeConfiguredTargetRequest(
                name=ct.name,
                authorization_token=self.auth_token
                )

        fctr_request = self.stub.FinalizeConfiguredTarget(fctr)

        ftr = rsu.FinalizeTargetRequest(
                name=t.name,
                authorization_token=self.auth_token
                )

        ftr_request = self.stub.FinalizeTarget(ftr)

        return mtr_request, mctr_request, fctr_request, ftr_request
        
    def open(self, timeout=30):
        i = inv.Invocation()
        i.id.invocation_id = self.invocation_id
        i.name = self.invocation_path

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

        ccr_request = self.send_configuration()

        return cir_request, ccr_request

    def close(self):
        self.update_duration()

        fin = rsu.FinalizeInvocationRequest(
                name=self.invocation_path,
                authorization_token=self.auth_token
                )
        return self.stub.FinalizeInvocation(fin)

