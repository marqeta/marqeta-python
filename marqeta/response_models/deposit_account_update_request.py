from datetime import datetime, date
import json


class DepositAccountUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def allow_immediate_credit(self):
        return self.json_response.get('allow_immediate_credit', None)

    def __repr__(self):
        return '<Marqeta.response_models.deposit_account_update_request.DepositAccountUpdateRequest>'
