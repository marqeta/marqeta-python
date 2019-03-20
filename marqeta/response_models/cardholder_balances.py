from datetime import datetime, date
from marqeta.response_models.cardholder_balance import CardholderBalance
from marqeta.response_models.link import Link
import json

class CardholderBalances(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def gpa(self):
        if 'gpa' in self.json_response:
            return CardholderBalance(self.json_response['gpa'])

    @property
    def links(self):
        if 'links' in self.json_response:
            return [Link(val) for val in self.json_response['links']]

    def __repr__(self):
         return '<Marqeta.response_models.cardholder_balances.CardholderBalances>'