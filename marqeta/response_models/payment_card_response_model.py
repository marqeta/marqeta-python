from datetime import datetime


class PaymentCardResponseModel(object):

    def __init__(self, response):
        self.response = response

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def type(self):
        if 'type' in self.response:
            return self.response['type']

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def account_suffix(self):
        if 'account_suffix' in self.response:
            return self.response['account_suffix']

    @property
    def account_type(self):
        if 'account_type' in self.response:
            return self.response['account_type']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.response:
            return self.response['is_default_account']

    @property
    def exp_date(self):
        if 'exp_date' in self.response:
            return self.response['exp_date']

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.response:
            return self.response['business_token']
