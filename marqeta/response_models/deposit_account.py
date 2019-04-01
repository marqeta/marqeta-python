from datetime import datetime, date
import json


class DepositAccount(object):

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
    def routing_number(self):
        return self.json_response.get('routing_number', None)

    @property
    def allow_immediate_credit(self):
        return self.json_response.get('allow_immediate_credit', None)

    def __repr__(self):
        return '<Marqeta.response_models.deposit_account.DepositAccount>' + self.__str__()
