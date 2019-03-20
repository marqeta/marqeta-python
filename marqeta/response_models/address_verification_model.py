from datetime import datetime, date
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.response import Response
import json

class AddressVerificationModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.address_verification_model.AddressVerificationModel>'