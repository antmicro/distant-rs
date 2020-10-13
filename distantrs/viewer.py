import distantrs as drs
from distantrs import get_grpcs_channel

class InvocationViewer:
    def __init__(self, invocation_id):
        self.channel = get_grpcs_channel()
        self.invocation_id = invocation_id
        self.invocation_path = f'invocations/{self.invocation_id}'
        self.stub = drs.rs_grpc.ResultStoreDownloadStub(self.channel)

    def __get_field_mask(self, proto, prefix=""):
        fields = []

        for f in proto.DESCRIPTOR.fields_by_name:
            fields.append(f'{prefix}{f}')

        fieldmask = [('X-Goog-FieldMask'.lower(), ",".join(fields))]
        return fieldmask

    def get_invocation(self):
        fieldmask = self.__get_field_mask(drs.inv.Invocation())
        request = drs.rs.GetInvocationRequest(name=self.invocation_path)

        return self.stub.GetInvocation(request=request, metadata=fieldmask)

    def list_configurations(self):
        # Fieldmask for ListConfigurations endpoint requires listing all nested 'configurations' fields
        # derived from the Configuration proto message.
        fieldmask_conf = self.__get_field_mask(drs.inv_conf.Configuration(), prefix="configurations.")
        fieldmask = [('X-Goog-FieldMask'.lower(), f"next_page_token,{fieldmask_conf[0][1]}")]

        print(fieldmask)
        
        request = drs.rs.ListConfigurationsRequest(
                parent=self.invocation_path,
                page_size=0,
                )
        return self.stub.ListConfigurations(request=request, metadata=fieldmask)
