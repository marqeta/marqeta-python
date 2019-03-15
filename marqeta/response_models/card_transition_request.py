from datetime import datetime, date
from marqeta.response_models.validations_request import ValidationsRequest
import json

class CardTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'card_token' : self.card_token,
           'reason' : self.reason,
           'reason_code' : self.reason_code,
           'validations' : self.validations,
           'channel' : self.channel,
           'state' : self.state,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def validations(self):
        if 'validations' in self.json_response:
            return ValidationsRequest(self.json_response['validations'])

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    def __repr__(self):
         return '<Marqeta.response_models.card_transition_request.CardTransitionRequest>'