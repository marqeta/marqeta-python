from datetime import datetime, date
import json

class ProgramReserveDepositRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'idempotentHash' : self.idempotentHash,
           'token' : self.token,
           'amount' : self.amount,
           'currency_code' : self.currency_code,
           'memo' : self.memo,
           'tags' : self.tags,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def idempotentHash(self):
        if 'idempotentHash' in self.json_response:
            return self.json_response['idempotentHash']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    def __repr__(self):
         return '<Marqeta.response_models.program_reserve_deposit_request.ProgramReserveDepositRequest>'