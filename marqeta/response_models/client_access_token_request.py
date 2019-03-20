from datetime import datetime, date
import json

class ClientAccessTokenRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def application_token(self):
        if 'application_token' in self.json_response:
            return self.json_response['application_token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    def __repr__(self):
         return '<Marqeta.response_models.client_access_token_request.ClientAccessTokenRequest>'