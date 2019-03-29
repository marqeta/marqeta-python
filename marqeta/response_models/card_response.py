from datetime import datetime, date
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.activation_actions import ActivationActions
import json


class CardResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):

        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):

        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token(self):

        return self.json_response.get('token', None)

    @property
    def user_token(self):

        return self.json_response.get('user_token', None)

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

        if 'expiration_time' in self.json_response:
            return datetime.strptime(self.json_response['expiration_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def cvv_number(self):

        return self.json_response.get('cvv_number', None)

    @property
    def chip_cvv_number(self):

        return self.json_response.get('chip_cvv_number', None)

    @property
    def barcode(self):

        return self.json_response.get('barcode', None)

    @property
    def pin_is_set(self):

        return self.json_response.get('pin_is_set', None)

    @property
    def state(self):

        return self.json_response.get('state', None)

    @property
    def state_reason(self):

        return self.json_response.get('state_reason', None)

    @property
    def fulfillment_status(self):

        return self.json_response.get('fulfillment_status', None)

    @property
    def reissue_pan_from_card_token(self):

        return self.json_response.get('reissue_pan_from_card_token', None)

    @property
    def fulfillment(self):

        if 'fulfillment' in self.json_response:
            return CardFulfillmentResponse(self.json_response['fulfillment'])

    @property
    def bulk_issuance_token(self):

        return self.json_response.get('bulk_issuance_token', None)

    @property
    def translate_pin_from_card_token(self):

        return self.json_response.get('translate_pin_from_card_token', None)

    @property
    def activation_actions(self):

        if 'activation_actions' in self.json_response:
            return ActivationActions(self.json_response['activation_actions'])

    @property
    def instrument_type(self):

        return self.json_response.get('instrument_type', None)

    @property
    def expedite(self):

        return self.json_response.get('expedite', None)

    @property
    def metadata(self):

        return self.json_response.get('metadata', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_response.CardResponse>'
