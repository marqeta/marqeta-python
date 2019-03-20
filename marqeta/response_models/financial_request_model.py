from datetime import datetime, date
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
from marqeta.response_models.transaction_options import TransactionOptions
from marqeta.response_models.webhook import Webhook
import json

class FinancialRequestModel(object):

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
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def pin(self):
        if 'pin' in self.json_response:
            return self.json_response['pin']

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def cash_back_amount(self):
        if 'cash_back_amount' in self.json_response:
            return self.json_response['cash_back_amount']

    @property
    def is_pre_auth(self):
        if 'is_pre_auth' in self.json_response:
            return self.json_response['is_pre_auth']

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    @property
    def transaction_options(self):
        if 'transaction_options' in self.json_response:
            return TransactionOptions(self.json_response['transaction_options'])

    @property
    def webhook(self):
        if 'webhook' in self.json_response:
            return Webhook(self.json_response['webhook'])

    def __repr__(self):
         return '<Marqeta.response_models.financial_request_model.FinancialRequestModel>'