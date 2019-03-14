from datetime import datetime, date
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
from marqeta.response_models.webhook import Webhook
import json

class WithdrawalRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'account_type' : self.account_type,
           'card_token' : self.card_token,
           'pin' : self.pin,
           'mid' : self.mid,
           'amount' : self.amount,
           'card_acceptor' : self.card_acceptor,
           'webhook' : self.webhook,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def account_type(self):
        if 'account_type' in self.json_response:
            return self.json_response['account_type']

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
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    @property
    def webhook(self):
        if 'webhook' in self.json_response:
            return Webhook(self.json_response['webhook'])

    def __repr__(self):
         return '<Marqeta.response_models.withdrawal_request_model.WithdrawalRequestModel>'