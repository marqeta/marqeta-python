from datetime import datetime
from marqeta.response_models.gatewaylog import Gatewaylog

class FundingResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def accounting_balance(self):
        if 'accounting_balance' in self.json_response:
            return self.json_response['accounting_balance']

    @property
    def available_balance(self):
        if 'available_balance' in self.json_response:
            return self.json_response['available_balance']

    @property
    def transaction(self):
        if 'transaction' in self.json_response:
            return Gatewaylog(self.json_response['transaction'])

