import distantrs as drs

class InvocationViewer:
    def __init__(self, invocation_id, channel=None):
        self.channel = channel or drs.get_grpcs_channel()
        self.invocation_id = invocation_id
        self.invocation_path = f'invocations/{self.invocation_id}'
        self.stub = drs.rs_grpc.ResultStoreDownloadStub(self.channel)

    def __get_field_mask(self, proto, prefix="", additional_fields=[]):
        """Returns a fieldmask with all fields from the proto message (no recursion)
        in a form of a list of metadata ready to be used in stub request.

        Example usage: stub.SayHello(request=request, metadata=fieldmask

        Args:
            proto - an instantiated protobuf message, 
                e.g. google.protobuf.timestamp_pb2.Timestamp()
            prefix - optional, string; prefix for field names
            additional_fields - optional, list; additional fields for mask
        """
        fields = []

        for f in proto.DESCRIPTOR.fields_by_name:
            fields.append(f'{prefix}{f}')

        fields.extend(additional_fields)

        fieldmask = [('X-Goog-FieldMask'.lower(), ",".join(fields))]
        return fieldmask

    def get_invocation(self):
        fieldmask = self.__get_field_mask(drs.inv.Invocation())
        request = drs.rs.GetInvocationRequest(name=self.invocation_path)

        return self.stub.GetInvocation(request=request, metadata=fieldmask)

    def list_configurations(self):
        # Fieldmask for ListConfigurations endpoint requires listing all nested 'configurations' fields
        # derived from the Configuration proto message.
        fieldmask = self.__get_field_mask(
                drs.inv_conf.Configuration(), 
                prefix="configurations.",
                additional_fields=['next_page_token'],
                )

        request = drs.rs.ListConfigurationsRequest(
                parent=self.invocation_path,
                page_size=0,
                )
        return self.stub.ListConfigurations(request=request, metadata=fieldmask)

    def list_actions(self):
        fieldmask = self.__get_field_mask(
                drs.inv_act.Action(),
                prefix="actions.",
                additional_fields=['next_page_token'],
                )

        request = drs.rs.ListActionsRequest(
                parent=f'{self.invocation_path}/targets/-/configuredTargets/-',
                page_size=0,
                )
        return self.stub.ListActions(request=request, metadata=fieldmask)
