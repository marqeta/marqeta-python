from datetime import datetime, date
import json

class AuthUserUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'password' : self.password,
           'active' : self.active,
           'roles' : self.roles,
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

    def __repr__(self):
         return '<Marqeta.response_models.auth_user_update_request.AuthUserUpdateRequest>'