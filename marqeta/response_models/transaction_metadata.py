from datetime import datetime
from marqeta.response_models.transit import Transit
from marqeta.response_models.airline import Airline

class TransactionMetadata(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transaction_category(self):
        if 'transaction_category' in self.json_response:
            return self.json_response['transaction_category']

    @property
    def payment_channel(self):
        if 'payment_channel' in self.json_response:
            return self.json_response['payment_channel']

    @property
    def cross_border_transaction(self):
        if 'cross_border_transaction' in self.json_response:
            return self.json_response['cross_border_transaction']

    @property
    def authorization_life_cyle(self):
        if 'authorization_life_cyle' in self.json_response:
            return self.json_response['authorization_life_cyle']

    @property
    def is_lodging_auto_rental(self):
        if 'is_lodging_auto_rental' in self.json_response:
            return self.json_response['is_lodging_auto_rental']

    @property
    def lodging_auto_rental_start_date(self):
        if 'lodging_auto_rental_start_date' in self.json_response:
            return datetime.strptime(self.json_response['lodging_auto_rental_start_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def transit(self):
        if 'transit' in self.json_response:
            return Transit(self.json_response['transit'])

    @property
    def airline(self):
        if 'airline' in self.json_response:
            return Airline(self.json_response['airline'])

