from datetime import datetime

class GatewayProgramFundingSourceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def url(self):
        if 'url' in self.json_response:
            return self.json_response['url']

    @property
    def version(self):
        if 'version' in self.json_response:
            return self.json_response['version']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def account(self):
        if 'account' in self.json_response:
            return self.json_response['account']

    @property
    def basic_auth_username(self):
        if 'basic_auth_username' in self.json_response:
            return self.json_response['basic_auth_username']

    @property
    def basic_auth_password(self):
        if 'basic_auth_password' in self.json_response:
            return self.json_response['basic_auth_password']

    @property
    def timeout_millis(self):
        if 'timeout_millis' in self.json_response:
            return self.json_response['timeout_millis']

