from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.response import Response


class AddressVerificationSource(object):

    def __init__(self, response):
        self.response = response

    @property
    def on_file(self):
        if 'on_file' in self.response:
            return AvsInformation(self.response['on_file'])

    @property
    def response(self):
        if 'response' in self.response:
            return Response(self.response['response'])
