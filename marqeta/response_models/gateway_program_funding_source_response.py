from datetime import datetime, date
import json


class GatewayProgramFundingSourceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get('name', None)

    @property
    def url(self):
        return self.json_response.get('url', None)

    @property
    def version(self):
        return self.json_response.get('version', None)

    @property
    def active(self):

        return self.json_response.get('active', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

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
        return self.json_response.get('account', None)

    @property
    def basic_auth_username(self):
        return self.json_response.get('basic_auth_username', None)

    @property
    def basic_auth_password(self):
        return self.json_response.get('basic_auth_password', None)

    @property
    def timeout_millis(self):
        return self.json_response.get('timeout_millis', None)

    def __repr__(self):
        return '<Marqeta.response_models.gateway_program_funding_source_response.GatewayProgramFundingSourceResponse>'\
               + self.__str__()
