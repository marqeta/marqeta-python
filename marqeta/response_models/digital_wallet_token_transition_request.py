from datetime import datetime, date
from marqeta.response_models.digital_wallet_token_hash import DigitalWalletTokenHash
import json


class DigitalWalletTokenTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def token_reference_id(self):
        return self.json_response.get('token_reference_id', None)

    @property
    def channel(self):
        return self.json_response.get('channel', None)

    @property
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletTokenHash(self.json_response['digital_wallet_token'])

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def reason(self):
        return self.json_response.get('reason', None)

    @property
    def override_tsp_error(self):
        return self.json_response.get('override_tsp_error', None)

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_token_transition_request.DigitalWalletTokenTransitionRequest>'
