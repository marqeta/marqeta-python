from datetime import datetime

class PasswordUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def new_password(self):
        if 'new_password' in self.json_response:
            return self.json_response['new_password']

    @property
    def current_password(self):
        if 'current_password' in self.json_response:
            return self.json_response['current_password']

