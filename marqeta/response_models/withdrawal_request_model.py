from datetime import datetime
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
from marqeta.response_models.webhook import Webhook

class WithdrawalRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

