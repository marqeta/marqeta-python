from datetime import datetime

class AuthUserUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def password(self):
        if 'password' in self.json_response:
            return self.json_response['password']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def roles(self):
        if 'roles' in self.json_response:
            return self.json_response['roles']

