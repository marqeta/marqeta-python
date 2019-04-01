from datetime import datetime, date
from marqeta.response_models.jit_funding_api import JitFundingApi
import json


class JitProgramResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def jit_funding(self):
        if 'jit_funding' in self.json_response:
            return JitFundingApi(self.json_response['jit_funding'])

    def __repr__(self):
        return '<Marqeta.response_models.jit_program_response.JitProgramResponse>' + self.__str__()
