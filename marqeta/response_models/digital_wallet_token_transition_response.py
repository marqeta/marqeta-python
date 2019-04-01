from datetime import datetime, date
from marqeta.response_models.digital_wallet_token_hash import DigitalWalletTokenHash
from marqeta.response_models.card_swap_hash import CardSwapHash
import json


class DigitalWalletTokenTransitionResponse(object):

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
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletTokenHash(self.json_response['digital_wallet_token'])

    @property
    def card_swap(self):
        if 'card_swap' in self.json_response:
            return CardSwapHash(self.json_response['card_swap'])

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def channel(self):
        return self.json_response.get('channel', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def fulfillment_status(self):
        return self.json_response.get('fulfillment_status', None)

    @property
    def reason(self):
        return self.json_response.get('reason', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_token_transition_response.' \
               'DigitalWalletTokenTransitionResponse>' + self.__str__()
