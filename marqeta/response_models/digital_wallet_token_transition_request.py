from datetime import datetime, date
from marqeta.response_models.digital_wallet_token_hash import DigitalWalletTokenHash
import json

class DigitalWalletTokenTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'reason_code' : self.reason_code,
           'token_reference_id' : self.token_reference_id,
           'channel' : self.channel,
           'digital_wallet_token' : self.digital_wallet_token,
           'state' : self.state,
           'reason' : self.reason,
           'override_tsp_error' : self.override_tsp_error,
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
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def token_reference_id(self):
        if 'token_reference_id' in self.json_response:
            return self.json_response['token_reference_id']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletTokenHash(self.json_response['digital_wallet_token'])

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def override_tsp_error(self):
        if 'override_tsp_error' in self.json_response:
            return self.json_response['override_tsp_error']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_transition_request.DigitalWalletTokenTransitionRequest>'