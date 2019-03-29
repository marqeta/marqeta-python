from datetime import datetime, date
import json


class ProgramReserveDepositRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def idempotentHash(self):
        return self.json_response.get('idempotentHash', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)

    @property
    def memo(self):
        return self.json_response.get('memo', None)

    @property
    def tags(self):
        return self.json_response.get('tags', None)

    def __repr__(self):
        return '<Marqeta.response_models.program_reserve_deposit_request.ProgramReserveDepositRequest>'
