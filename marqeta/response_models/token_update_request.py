from datetime import datetime, date
import json

class TokenUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def exp_date(self):
        if 'exp_date' in self.json_response:
            return self.json_response['exp_date']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.json_response:
            return self.json_response['is_default_account']

    def __repr__(self):
         return '<Marqeta.response_models.token_update_request.TokenUpdateRequest>'