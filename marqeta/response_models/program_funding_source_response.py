from datetime import datetime


class ProgramFundingSourceResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def account(self):
        if 'account' in self.response:
            return self.response['account']
