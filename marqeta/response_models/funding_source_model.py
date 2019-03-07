from datetime import datetime


class FundingSourceModel(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.response:
            return self.response['is_default_account']

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
