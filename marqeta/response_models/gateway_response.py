from datetime import datetime, date
from marqeta.response_models.jit_program_response import JitProgramResponse
import json


class GatewayResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def code(self):
        return self.json_response.get('code', None)

    @property
    def data(self):
        if 'data' in self.json_response:
            return JitProgramResponse(self.json_response['data'])

    def __repr__(self):
        return '<Marqeta.response_models.gateway_response.GatewayResponse>' + self.__str__()
