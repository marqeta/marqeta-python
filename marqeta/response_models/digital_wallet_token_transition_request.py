from datetime import datetime
from marqeta.response_models.digital_wallet_token_hash import DigitalWalletTokenHash

class DigitalWalletTokenTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

