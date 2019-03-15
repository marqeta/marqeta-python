from datetime import datetime, date
import json

class GatewayProgramFundingSourceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'url' : self.url,
           'version' : self.version,
           'active' : self.active,
           'token' : self.token,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'account' : self.account,
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

    def __repr__(self):
         return '<Marqeta.response_models.gateway_program_funding_source_response.GatewayProgramFundingSourceResponse>'