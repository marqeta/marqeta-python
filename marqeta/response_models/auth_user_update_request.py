from datetime import datetime, date
import json


class AuthUserUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def password(self):
        return self.json_response.get('password', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def roles(self):
        return self.json_response.get('roles', None)

    def __repr__(self):
        return '<Marqeta.response_models.auth_user_update_request.AuthUserUpdateRequest>' + self.__str__()
