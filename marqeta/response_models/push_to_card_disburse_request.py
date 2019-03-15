from datetime import datetime, date
import json

class PushToCardDisburseRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'tags' : self.tags,
           'memo' : self.memo,
           'token' : self.token,
           'currency_code' : self.currency_code,
           'amount' : self.amount,
           'payment_instrument_token' : self.payment_instrument_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def payment_instrument_token(self):
        if 'payment_instrument_token' in self.json_response:
            return self.json_response['payment_instrument_token']

    def __repr__(self):
         return '<Marqeta.response_models.push_to_card_disburse_request.PushToCardDisburseRequest>'