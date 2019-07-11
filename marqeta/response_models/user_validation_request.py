from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class UserValidationRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def birth_date(self):
        if 'birth_date' in self.json_response:
            return datetime_object('birth_date', self.json_response)


    @property
    def phone(self):
        return self.json_response.get('phone', None)


    @property
    def ssn(self):
        return self.json_response.get('ssn', None)


    def __repr__(self):
         return '<Marqeta.response_models.user_validation_request.UserValidationRequest>' + self.__str__()
