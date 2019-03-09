from datetime import datetime
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.response import Response

class AddressVerificationModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def request(self):
        if 'request' in self.json_response:
            return AvsInformation(self.json_response['request'])

    @property
    def on_file(self):
        if 'on_file' in self.json_response:
            return AvsInformation(self.json_response['on_file'])

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

