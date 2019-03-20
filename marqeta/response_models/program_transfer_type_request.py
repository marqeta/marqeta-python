from datetime import datetime, date
import json

class ProgramTransferTypeRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def program_funding_source_token(self):
        if 'program_funding_source_token' in self.json_response:
            return self.json_response['program_funding_source_token']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    def __repr__(self):
         return '<Marqeta.response_models.program_transfer_type_request.ProgramTransferTypeRequest>'