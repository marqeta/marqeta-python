"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.card_metadata import CardMetadata
from marqeta.response_models.cardholder_metadata import CardholderMetadata


class CardTransitionResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def card_token(self):
        if 'card_token' in self.response:
            return self.response['card_token']

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def state(self):
        if 'state' in self.response:
            return self.response['state']

    @property
    def reason(self):
        if 'reason' in self.response:
            return self.response['reason']

    @property
    def reason_code(self):
        if 'reason_code' in self.response:
            return self.response['reason_code']

    @property
    def channel(self):
        if 'channel' in self.response:
            return self.response['channel']

    @property
    def fulfillment_status(self):
        if 'fulfillment_status' in self.response:
            return self.response['fulfillment_status']

    @property
    def validations(self):
        if 'validations' in self.response:
            return ValidationResponse(self.response['validations'])

    @property
    def type(self):
        if 'type' in self.response:
            return self.response['type']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

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
            return self.response['expiration_time']

    @property
    def barcode(self):
        if 'barcode' in self.response:
            return self.response['barcode']

    @property
    def pin_is_set(self):
        if 'pin_is_set' in self.response:
            return self.response['pin_is_set']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.response:
            return CardFulfillmentResponse(self.response['fulfillment'])

    @property
    def bulk_issuance_token(self):
        if 'bulk_issuance_token' in self.response:
            return self.response['bulk_issuance_token']

    @property
    def reissue_pan_from_card_token(self):
        if 'reissue_pan_from_card_token' in self.response:
            return self.response['reissue_pan_from_card_token']

    @property
    def user(self):
        if 'user' in self.response:
            return CardholderMetadata(self.response['user'])

    @property
    def card(self):
        if 'card' in self.response:
            return CardMetadata(self.response['card'])

    @property
    def expedite(self):
        if 'expedite' in self.response:
            return self.response['expedite']


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