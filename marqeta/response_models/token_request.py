from datetime import datetime, date
import json


class TokenRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def account_number(self):
        return self.json_response.get('account_number', None)

    @property
    def cvv_number(self):
        return self.json_response.get('cvv_number', None)

    @property
    def exp_date(self):
        return self.json_response.get('exp_date', None)

    @property
    def zip(self):
        return self.json_response.get('zip', None)

    @property
    def postal_code(self):
        return self.json_response.get('postal_code', None)

    @property
    def is_default_account(self):
        return self.json_response.get('is_default_account', None)

    def __repr__(self):
        return '<Marqeta.response_models.token_request.TokenRequest>' + self.__str__()
