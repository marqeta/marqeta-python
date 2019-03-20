from datetime import datetime, date
from marqeta.response_models.poi import Poi
from marqeta.response_models.transaction_controls import TransactionControls
from marqeta.response_models.selective_auth import SelectiveAuth
from marqeta.response_models.special import Special
from marqeta.response_models.card_life_cycle import CardLifeCycle
from marqeta.response_models.clearing_and_settlement import ClearingAndSettlement
from marqeta.response_models.jit_funding import JitFunding
from marqeta.response_models.digital_wallet_tokenization import DigitalWalletTokenization
from marqeta.response_models.card_product_fulfillment import CardProductFulfillment
import json

class CardProductConfig(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def poi(self):
        if 'poi' in self.json_response:
            return Poi(self.json_response['poi'])

    @property
    def transaction_controls(self):
        if 'transaction_controls' in self.json_response:
            return TransactionControls(self.json_response['transaction_controls'])

    @property
    def selective_auth(self):
        if 'selective_auth' in self.json_response:
            return SelectiveAuth(self.json_response['selective_auth'])

    @property
    def special(self):
        if 'special' in self.json_response:
            return Special(self.json_response['special'])

    @property
    def card_life_cycle(self):
        if 'card_life_cycle' in self.json_response:
            return CardLifeCycle(self.json_response['card_life_cycle'])

    @property
    def clearing_and_settlement(self):
        if 'clearing_and_settlement' in self.json_response:
            return ClearingAndSettlement(self.json_response['clearing_and_settlement'])

    @property
    def jit_funding(self):
        if 'jit_funding' in self.json_response:
            return JitFunding(self.json_response['jit_funding'])

    @property
    def digital_wallet_tokenization(self):
        if 'digital_wallet_tokenization' in self.json_response:
            return DigitalWalletTokenization(self.json_response['digital_wallet_tokenization'])

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return CardProductFulfillment(self.json_response['fulfillment'])

    def __repr__(self):
         return '<Marqeta.response_models.card_product_config.CardProductConfig>'