from datetime import datetime, date
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
import json

class ClearingModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'network_fees' : self.network_fees,
           'webhook' : self.webhook,
           'is_refund' : self.is_refund,
           'force_post' : self.force_post,
           'amount' : self.amount,
           'original_transaction_token' : self.original_transaction_token,
           'mid' : self.mid,
           'card_acceptor' : self.card_acceptor,
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
    def is_refund(self):
        if 'is_refund' in self.json_response:
            return self.json_response['is_refund']

    @property
    def force_post(self):
        if 'force_post' in self.json_response:
            return self.json_response['force_post']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def original_transaction_token(self):
        if 'original_transaction_token' in self.json_response:
            return self.json_response['original_transaction_token']

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    def __repr__(self):
         return '<Marqeta.response_models.clearing_model.ClearingModel>'