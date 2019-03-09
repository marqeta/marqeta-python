from datetime import datetime
from marqeta.response_models.user_validation_request import UserValidationRequest

class ValidationsRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def user(self):
        if 'user' in self.json_response:
            return UserValidationRequest(self.json_response['user'])

