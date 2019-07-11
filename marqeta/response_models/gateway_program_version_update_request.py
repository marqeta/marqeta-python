from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class GatewayProgramVersionUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def version(self):
        return self.json_response.get('version', None)


    def __repr__(self):
         return '<Marqeta.response_models.gateway_program_version_update_request.GatewayProgramVersionUpdateRequest>' + self.__str__()
