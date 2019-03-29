from datetime import datetime, date
from marqeta.response_models.billing_address import BillingAddress
import json


class CardOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def cvv(self):

        return self.json_response.get('cvv', None)

    @property
    def card_present(self):

        return self.json_response.get('card_present', None)

    @property
    def expiration(self):

        return self.json_response.get('expiration', None)

    @property
    def billing_address(self):

        if 'billing_address' in self.json_response:
            return BillingAddress(self.json_response['billing_address'])

    def __repr__(self):
        return '<Marqeta.response_models.card_options.CardOptions>'
