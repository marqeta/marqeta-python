from datetime import datetime, date
import json

class GatewayProgramFundingSourceRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'token' : self.token,
           'active' : self.active,
           'url' : self.url,
           'basic_auth_username' : self.basic_auth_username,
           'basic_auth_password' : self.basic_auth_password,
           'timeout_millis' : self.timeout_millis,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.gateway_program_funding_source_request.GatewayProgramFundingSourceRequest>'