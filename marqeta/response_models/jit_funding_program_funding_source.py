from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class JitFundingProgramFundingSource(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def enabled(self):
        return self.json_response.get('enabled', None)

    @property
    def funding_source_token(self):
        return self.json_response.get('funding_source_token', None)


    @property
    def refunds_destination(self):
        return self.json_response.get('refunds_destination', None)


    def __repr__(self):
         return '<Marqeta.response_models.jit_funding_program_funding_source.JitFundingProgramFundingSource>' + self.__str__()
