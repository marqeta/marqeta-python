from datetime import datetime
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.activation_actions import ActivationActions

class CardResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

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
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def card_product_token(self):
        if 'card_product_token' in self.json_response:
            return self.json_response['card_product_token']

    @property
    def last_four(self):
        if 'last_four' in self.json_response:
            return self.json_response['last_four']

    @property
    def pan(self):
        if 'pan' in self.json_response:
            return self.json_response['pan']

    @property
    def expiration(self):
        if 'expiration' in self.json_response:
            return self.json_response['expiration']

    @property
    def expiration_time(self):
        if 'expiration_time' in self.json_response:
            return datetime.strptime(self.json_response['expiration_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def cvv_number(self):
        if 'cvv_number' in self.json_response:
            return self.json_response['cvv_number']

    @property
    def chip_cvv_number(self):
        if 'chip_cvv_number' in self.json_response:
            return self.json_response['chip_cvv_number']

    @property
    def barcode(self):
        if 'barcode' in self.json_response:
            return self.json_response['barcode']

    @property
    def pin_is_set(self):
        if 'pin_is_set' in self.json_response:
            return self.json_response['pin_is_set']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def state_reason(self):
        if 'state_reason' in self.json_response:
            return self.json_response['state_reason']

    @property
    def fulfillment_status(self):
        if 'fulfillment_status' in self.json_response:
            return self.json_response['fulfillment_status']

    @property
    def reissue_pan_from_card_token(self):
        if 'reissue_pan_from_card_token' in self.json_response:
            return self.json_response['reissue_pan_from_card_token']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return CardFulfillmentResponse(self.json_response['fulfillment'])

    @property
    def bulk_issuance_token(self):
        if 'bulk_issuance_token' in self.json_response:
            return self.json_response['bulk_issuance_token']

    @property
    def translate_pin_from_card_token(self):
        if 'translate_pin_from_card_token' in self.json_response:
            return self.json_response['translate_pin_from_card_token']

    @property
    def activation_actions(self):
        if 'activation_actions' in self.json_response:
            return ActivationActions(self.json_response['activation_actions'])

    @property
    def instrument_type(self):
        if 'instrument_type' in self.json_response:
            return self.json_response['instrument_type']

    @property
    def expedite(self):
        if 'expedite' in self.json_response:
            return self.json_response['expedite']

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

