from datetime import datetime
from marqeta.response_models.digital_wallet_token_hash import DigitalWalletTokenHash
from marqeta.response_models.card_swap_hash import CardSwapHash

class DigitalWalletTokenTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletTokenHash(self.json_response['digital_wallet_token'])

    @property
    def card_swap(self):
        if 'card_swap' in self.json_response:
            return CardSwapHash(self.json_response['card_swap'])

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def fulfillment_status(self):
        if 'fulfillment_status' in self.json_response:
            return self.json_response['fulfillment_status']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

