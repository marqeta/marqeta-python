"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.card_metadata import CardMetadata
from marqeta.response_models.cardholder_metadata import CardholderMetadata


class CardTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def fulfillment_status(self):
        if 'fulfillment_status' in self.json_response:
            return self.json_response['fulfillment_status']

    @property
    def validations(self):
        if 'validations' in self.json_response:
            return ValidationResponse(self.json_response['validations'])

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

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
            return self.json_response['expiration_time']

    @property
    def barcode(self):
        if 'barcode' in self.json_response:
            return self.json_response['barcode']

    @property
    def pin_is_set(self):
        if 'pin_is_set' in self.json_response:
            return self.json_response['pin_is_set']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return CardFulfillmentResponse(self.json_response['fulfillment'])

    @property
    def bulk_issuance_token(self):
        if 'bulk_issuance_token' in self.json_response:
            return self.json_response['bulk_issuance_token']

    @property
    def reissue_pan_from_card_token(self):
        if 'reissue_pan_from_card_token' in self.json_response:
            return self.json_response['reissue_pan_from_card_token']

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
        if 'expedite' in self.json_response:
            return self.json_response['expedite']


class ValidationResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def user(self):
        if 'user' in self.response:
            return UserValidationResponse(self.response['user'])


class UserValidationResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def birth_date(self):
        if 'birth_date' in self.response:
            return self.response['birth_date']

    @property
    def phone(self):
        if 'phone' in self.response:
            return self.response['phone']

    @property
    def ssn(self):
        if 'ssn' in self.response:
            return self.response['ssn']
