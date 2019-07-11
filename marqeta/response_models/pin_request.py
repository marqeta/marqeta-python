from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class PinRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def control_token(self):
        return self.json_response.get('control_token', None)


    @property
    def pin(self):
        return self.json_response.get('pin', None)


    def __repr__(self):
         return '<Marqeta.response_models.pin_request.PinRequest>' + self.__str__()
