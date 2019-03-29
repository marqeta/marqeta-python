from datetime import datetime, date
from marqeta.response_models.user_validation_response import UserValidationResponse
import json


class ValidationsResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user(self):

        if 'user' in self.json_response:
            return UserValidationResponse(self.json_response['user'])

    def __repr__(self):
        return '<Marqeta.response_models.validations_response.ValidationsResponse>'
