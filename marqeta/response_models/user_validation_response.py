from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class UserValidationResponse(object):

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
        return self.json_response.get('birth_date', None)

    @property
    def phone(self):
        return self.json_response.get('phone', None)

    @property
    def ssn(self):
        return self.json_response.get('ssn', None)

    def __repr__(self):
         return '<Marqeta.response_models.user_validation_response.UserValidationResponse>' + self.__str__()
