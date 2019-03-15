from datetime import datetime, date
import json

class ReplacementAmount(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'transaction_amount' : self.transaction_amount,
           'settlement_amount' : self.settlement_amount,
           'transaction_fee' : self.transaction_fee,
           'settlement_fee' : self.settlement_fee,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_amount(self):
        if 'transaction_amount' in self.json_response:
            return self.json_response['transaction_amount']

    @property
    def settlement_amount(self):
        if 'settlement_amount' in self.json_response:
            return self.json_response['settlement_amount']

    @property
    def transaction_fee(self):
        if 'transaction_fee' in self.json_response:
            return self.json_response['transaction_fee']

    @property
    def settlement_fee(self):
        if 'settlement_fee' in self.json_response:
            return self.json_response['settlement_fee']

    def __repr__(self):
         return '<Marqeta.response_models.replacement_amount.ReplacementAmount>'