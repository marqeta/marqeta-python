from datetime import datetime
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.response import Response

class AddressVerificationSource(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def on_file(self):
        if 'on_file' in self.json_response:
            return AvsInformation(self.json_response['on_file'])

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

