from datetime import datetime, date
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.transaction_options import TransactionOptions
import json


class AuthorizationAdviceModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def amount(self):
        return self.json_response.get('amount', None)

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
        return self.json_response.get('original_transaction_token', None)

    @property
    def transaction_options(self):
        if 'transaction_options' in self.json_response:
            return TransactionOptions(self.json_response['transaction_options'])

    def __repr__(self):
        return '<Marqeta.response_models.authorization_advice_model.AuthorizationAdviceModel>'
