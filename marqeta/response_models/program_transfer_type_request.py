from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

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
        return self.json_response.get('token', None)


    @property
    def program_funding_source_token(self):
        return self.json_response.get('program_funding_source_token', None)


    @property
    def tags(self):
        return self.json_response.get('tags', None)


    @property
    def memo(self):
        return self.json_response.get('memo', None)


    def __repr__(self):
         return '<Marqeta.response_models.program_transfer_type_request.ProgramTransferTypeRequest>' + self.__str__()
