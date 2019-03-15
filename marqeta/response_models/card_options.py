from datetime import datetime, date
from marqeta.response_models.billing_address import BillingAddress
import json

class CardOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'cvv' : self.cvv,
           'card_present' : self.card_present,
           'expiration' : self.expiration,
           'billing_address' : self.billing_address,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.card_options.CardOptions>'