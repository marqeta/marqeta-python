"""Deposit Account Model with Account Properties!!!"""


class DepositAccount(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.response:
            return self.response['business_token']

    @property
    def account_number(self):
        if 'account_number' in self.response:
            return self.response['account_number']

    @property
    def routing_number(self):
        if 'routing_number' in self.response:
            return self.response['routing_number']

    @property
    def allow_immediate_credit(self):
        if 'allow_immediate_credit' in self.response:
            return self.response['allow_immediate_credit']
