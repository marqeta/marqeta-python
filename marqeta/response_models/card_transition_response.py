from datetime import datetime, date
from marqeta.response_models.validations_response import ValidationsResponse
from marqeta.response_models.fulfillment import Fulfillment
from marqeta.response_models.cardholder_metadata import CardholderMetadata
from marqeta.response_models.card_metadata import CardMetadata
import json


class CardTransitionResponse(object):

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
    def card_token(self):
        return self.json_response.get('card_token', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def reason(self):
        return self.json_response.get('reason', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def channel(self):
        return self.json_response.get('channel', None)

    @property
    def fulfillment_status(self):
        return self.json_response.get('fulfillment_status', None)

    @property
    def validations(self):
        if 'validations' in self.json_response:
            return ValidationsResponse(self.json_response['validations'])

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def card_product_token(self):
        return self.json_response.get('card_product_token', None)

    @property
    def last_four(self):
        return self.json_response.get('last_four', None)

    @property
    def pan(self):
        return self.json_response.get('pan', None)

    @property
    def expiration(self):
        return self.json_response.get('expiration', None)

    @property
    def expiration_time(self):
        return self.json_response.get('expiration_time', None)

    @property
    def barcode(self):
        return self.json_response.get('barcode', None)

    @property
    def pin_is_set(self):
        return self.json_response.get('pin_is_set', None)

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return Fulfillment(self.json_response['fulfillment'])

    @property
    def bulk_issuance_token(self):
        return self.json_response.get('bulk_issuance_token', None)

    @property
    def reissue_pan_from_card_token(self):
        return self.json_response.get('reissue_pan_from_card_token', None)

    @property
    def user(self):
        if 'user' in self.json_response:
            return CardholderMetadata(self.json_response['user'])

    @property
    def card(self):
        if 'card' in self.json_response:
            return CardMetadata(self.json_response['card'])

    @property
    def expedite(self):
        return self.json_response.get('expedite', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_transition_response.CardTransitionResponse>' + self.__str__()
