from datetime import datetime, date
import json

class NetworkFeeModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def credit_debit(self):
        if 'credit_debit' in self.json_response:
            return self.json_response['credit_debit']

    def __repr__(self):
         return '<Marqeta.response_models.network_fee_model.NetworkFeeModel>'