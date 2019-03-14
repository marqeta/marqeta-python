from datetime import datetime, date
import json

class AuthUserRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'password' : self.password,
           'active' : self.active,
           'roles' : self.roles,
           'username' : self.username,
           'token' : self.token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    @property
    def username(self):
        if 'username' in self.json_response:
            return self.json_response['username']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    def __repr__(self):
         return '<Marqeta.response_models.auth_user_request.AuthUserRequest>'