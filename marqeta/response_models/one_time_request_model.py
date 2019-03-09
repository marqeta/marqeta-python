from datetime import datetime

class OneTimeRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

    @property
    def password(self):
        if 'password' in self.json_response:
            return self.json_response['password']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

