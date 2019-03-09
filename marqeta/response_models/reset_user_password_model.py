from datetime import datetime

class ResetUserPasswordModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def new_password(self):
        if 'new_password' in self.json_response:
            return self.json_response['new_password']

