from datetime import datetime, date
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
import json


class BalanceInquiryRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

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
    def account_type(self):
        return self.json_response.get('account_type', None)

    @property
    def card_token(self):
        return self.json_response.get('card_token', None)

    @property
    def pin(self):
        return self.json_response.get('pin', None)

    @property
    def mid(self):
        return self.json_response.get('mid', None)

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    def __repr__(self):
        return '<Marqeta.response_models.balance_inquiry_request_model.BalanceInquiryRequestModel>'
