from datetime import datetime, date
from marqeta.response_models.transit import Transit
from marqeta.response_models.airline import Airline
import json


class TransactionMetadata(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_category(self):

        return self.json_response.get('transaction_category', None)

    @property
    def payment_channel(self):

        return self.json_response.get('payment_channel', None)

    @property
    def cross_border_transaction(self):

        return self.json_response.get('cross_border_transaction', None)

    @property
    def authorization_life_cyle(self):

        return self.json_response.get('authorization_life_cyle', None)

    @property
    def is_lodging_auto_rental(self):

        return self.json_response.get('is_lodging_auto_rental', None)

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
