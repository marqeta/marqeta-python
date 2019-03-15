from datetime import datetime, date
import json

class ProgramFundingSourceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'active' : self.active,
           'token' : self.token,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'account' : self.account,
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

    def __repr__(self):
         return '<Marqeta.response_models.program_funding_source_response.ProgramFundingSourceResponse>'