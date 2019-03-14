from datetime import datetime, date
from marqeta.response_models.expiration_offsét import ExpirationOffsét
from marqeta.response_models.fulfillment import Fulfillment
from marqeta.response_models.activation_actions import ActivationActions
import json

class CardRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'card_product_token' : self.card_product_token,
           'expedite' : self.expedite,
           'metadata' : self.metadata,
           'expiration_offset' : self.expiration_offset,
           'token' : self.token,
           'user_token' : self.user_token,
           'fulfillment' : self.fulfillment,
           'reissue_pan_from_card_token' : self.reissue_pan_from_card_token,
           'translate_pin_from_card_token' : self.translate_pin_from_card_token,
           'activation_actions' : self.activation_actions,
           'bulk_issuance_token' : self.bulk_issuance_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_product_token(self):
        if 'card_product_token' in self.json_response:
            return self.json_response['card_product_token']

    @property
    def expedite(self):
        if 'expedite' in self.json_response:
            return self.json_response['expedite']

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffsét(self.json_response['expiration_offset'])

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return Fulfillment(self.json_response['fulfillment'])

    @property
    def reissue_pan_from_card_token(self):
        if 'reissue_pan_from_card_token' in self.json_response:
            return self.json_response['reissue_pan_from_card_token']

    @property
    def translate_pin_from_card_token(self):
        if 'translate_pin_from_card_token' in self.json_response:
            return self.json_response['translate_pin_from_card_token']

    @property
    def activation_actions(self):
        if 'activation_actions' in self.json_response:
            return ActivationActions(self.json_response['activation_actions'])

    @property
    def bulk_issuance_token(self):
        if 'bulk_issuance_token' in self.json_response:
            return self.json_response['bulk_issuance_token']

    def __repr__(self):
         return '<Marqeta.response_models.card_request.CardRequest>'