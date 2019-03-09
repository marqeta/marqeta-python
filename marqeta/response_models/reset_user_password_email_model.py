from datetime import datetime

class ResetUserPasswordEmailModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

