"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.activation_actions import ActivationActions


class CardResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def card_product_token(self):
        if 'card_product_token' in self.response:
            return self.response['card_product_token']

    @property
    def last_four(self):
        if 'last_four' in self.response:
            return self.response['last_four']

    @property
    def pan(self):
        if 'pan' in self.response:
            return self.response['pan']

    @property
    def expiration(self):
        if 'expiration' in self.response:
            return self.response['expiration']

    @property
    def expiration_time(self):
        if 'expiration_time' in self.response:
            return datetime.strptime(self.response['expiration_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def cvv_number(self):
        if 'cvv_number' in self.response:
            return self.response['cvv_number']

    @property
    def chip_cvv_number(self):
        if 'chip_cvv_number' in self.response:
            return self.response['chip_cvv_number']

    @property
    def barcode(self):
        if 'barcode' in self.response:
            return self.response['barcode']

    @property
    def pin_is_set(self):
        if 'pin_is_set' in self.response:
            return self.response['pin_is_set']

    @property
    def state(self):
        if 'state' in self.response:
            return self.response['state']

    @property
    def state_reason(self):
        if 'state_reason' in self.response:
            return self.response['state_reason']

    @property
    def fulfillment_status(self):
        if 'fulfillment_status' in self.response:
            return self.response['fulfillment_status']

    @property
    def reissue_pan_from_card_token(self):
        if 'reissue_pan_from_card_token' in self.response:
            return self.response['reissue_pan_from_card_token']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.response:
            return CardFulfillmentResponse(self.response['fulfillment'])

    @property
    def bulk_issuance_token(self):
        if 'bulk_issuance_token' in self.response:
            return self.response['bulk_issuance_token']

    @property
    def translate_pin_from_card_token(self):
        if 'translate_pin_from_card_token' in self.response:
            return self.response['translate_pin_from_card_token']

    @property
    def activation_actions(self):
        if 'activation_actions' in self.response:
            return ActivationActions(self.response['activation_actions'])

    @property
    def instrument_type(self):
        if 'instrument_type' in self.response:
            return self.response['instrument_type']

    @property
    def expedite(self):
        if 'expedite' in self.response:
            return self.response['expedite']

    @property
    def metadata(self):
        if 'metadata' in self.response:
            return self.response['metadata']
