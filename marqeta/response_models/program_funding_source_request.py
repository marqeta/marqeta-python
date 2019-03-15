from datetime import datetime, date
import json

class ProgramFundingSourceRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'active' : self.active,
           'token' : self.token,
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

    def __repr__(self):
         return '<Marqeta.response_models.program_funding_source_request.ProgramFundingSourceRequest>'