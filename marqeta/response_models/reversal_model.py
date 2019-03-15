from datetime import datetime, date
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
import json

class ReversalModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'network_fees' : self.network_fees,
           'webhook' : self.webhook,
           'original_transaction_token' : self.original_transaction_token,
           'amount' : self.amount,
           'find_original_window_days' : self.find_original_window_days,
           'is_advice' : self.is_advice,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network_fees(self):
        if 'network_fees' in self.json_response:
            return [NetworkFeeModel(val) for val in self.json_response['network_fees']]

    @property
    def webhook(self):
        if 'webhook' in self.json_response:
            return Webhook(self.json_response['webhook'])

    @property
    def original_transaction_token(self):
        if 'original_transaction_token' in self.json_response:
            return self.json_response['original_transaction_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def find_original_window_days(self):
        if 'find_original_window_days' in self.json_response:
            return self.json_response['find_original_window_days']

    @property
    def is_advice(self):
        if 'is_advice' in self.json_response:
            return self.json_response['is_advice']

    def __repr__(self):
         return '<Marqeta.response_models.reversal_model.ReversalModel>'