from datetime import datetime, date
import json

class ChargebackRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'transaction_token' : self.transaction_token,
           'amount' : self.amount,
           'reason_description' : self.reason_description,
           'reason_code' : self.reason_code,
           'memo' : self.memo,
           'credit_user' : self.credit_user,
           'channel' : self.channel,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def reason_description(self):
        if 'reason_description' in self.json_response:
            return self.json_response['reason_description']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def credit_user(self):
        if 'credit_user' in self.json_response:
            return self.json_response['credit_user']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    def __repr__(self):
         return '<Marqeta.response_models.chargeback_request.ChargebackRequest>'