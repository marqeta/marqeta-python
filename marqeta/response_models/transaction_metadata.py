from datetime import datetime, date
from marqeta.response_models.transit import Transit
from marqeta.response_models.airline import Airline
import json

class TransactionMetadata(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'transaction_category' : self.transaction_category,
           'payment_channel' : self.payment_channel,
           'cross_border_transaction' : self.cross_border_transaction,
           'authorization_life_cyle' : self.authorization_life_cyle,
           'is_lodging_auto_rental' : self.is_lodging_auto_rental,
           'lodging_auto_rental_start_date' : self.lodging_auto_rental_start_date,
           'transit' : self.transit,
           'airline' : self.airline,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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
                return datetime.strptime(self.json_response['lodging_auto_rental_start_date'], '%Y-%m-%d').date()

    @property
    def transit(self):
        if 'transit' in self.json_response:
            return Transit(self.json_response['transit'])

    @property
    def airline(self):
        if 'airline' in self.json_response:
            return Airline(self.json_response['airline'])

    def __repr__(self):
         return '<Marqeta.response_models.transaction_metadata.TransactionMetadata>'