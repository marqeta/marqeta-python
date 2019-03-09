from datetime import datetime
from marqeta.response_models.user_validation_response import UserValidationResponse

class ValidationsResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def user(self):
        if 'user' in self.json_response:
            return UserValidationResponse(self.json_response['user'])

