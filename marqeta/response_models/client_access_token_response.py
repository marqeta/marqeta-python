from datetime import datetime
from marqeta.response_models.application import Application

class ClientAccessTokenResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def application(self):
        if 'application' in self.json_response:
            return Application(self.json_response['application'])

    @property
    def created(self):
        if 'created' in self.json_response:
            return datetime.strptime(self.json_response['created'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def expires(self):
        if 'expires' in self.json_response:
            return datetime.strptime(self.json_response['expires'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

