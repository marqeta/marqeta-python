from datetime import datetime
from marqeta.response_models.billing_address import BillingAddress

class CardOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def cvv(self):
        if 'cvv' in self.json_response:
            return self.json_response['cvv']

    @property
    def card_present(self):
        if 'card_present' in self.json_response:
            return self.json_response['card_present']

    @property
    def expiration(self):
        if 'expiration' in self.json_response:
            return self.json_response['expiration']

    @property
    def billing_address(self):
        if 'billing_address' in self.json_response:
            return BillingAddress(self.json_response['billing_address'])

