from datetime import datetime

class GatewayProgramFundingSourceRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def url(self):
        if 'url' in self.json_response:
            return self.json_response['url']

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

