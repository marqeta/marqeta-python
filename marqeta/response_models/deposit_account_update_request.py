from datetime import datetime, date
import json

class DepositAccountUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'allow_immediate_credit' : self.allow_immediate_credit,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def allow_immediate_credit(self):
        if 'allow_immediate_credit' in self.json_response:
            return self.json_response['allow_immediate_credit']

    def __repr__(self):
         return '<Marqeta.response_models.deposit_account_update_request.DepositAccountUpdateRequest>'