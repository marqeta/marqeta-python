from datetime import datetime, date
import json

class MoneyModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'amount' : self.amount,
           'currency' : self.currency,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def currency(self):
        if 'currency' in self.json_response:
            return self.json_response['currency']

    def __repr__(self):
         return '<Marqeta.response_models.money_model.MoneyModel>'