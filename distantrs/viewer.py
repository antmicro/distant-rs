import distantrs as drs
from distantrs import get_grpcs_channel

class InvocationViewer:
    def __init__(self, invocation_id):
        self.channel = get_grpcs_channel()
        self.invocation_id = invocation_id
        self.stub = drs.rs_grpc.ResultStoreDownloadStub(self.channel)

    def __get_field_mask(self, proto):
        fields = []

        for f in proto.DESCRIPTOR.fields_by_name:
            fields.append(f)

        fieldmask = [('X-Goog-FieldMask'.lower(), ",".join(fields))]
        return fieldmask

    def get_invocation(self):
        fieldmask = self.__get_field_mask(drs.inv.Invocation())
        stub = drs.rs_grpc.ResultStoreDownloadStub(self.channel)
        request = drs.rs.GetInvocationRequest(name=f'invocations/{self.invocation_id}')

        return stub.GetInvocation(request=request, metadata=fieldmask)
