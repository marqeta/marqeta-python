from datetime import datetime, date
import json


class Authentication(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def last_password_update_channel(self):
        return self.json_response.get('last_password_update_channel', None)

    @property
    def last_password_update_time(self):
        if 'last_password_update_time' in self.json_response:
            return datetime.strptime(self.json_response['last_password_update_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def email_verified(self):
        return self.json_response.get('email_verified', None)

    @property
    def email_verified_time(self):
        if 'email_verified_time' in self.json_response:
            return datetime.strptime(self.json_response['email_verified_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.authentication.Authentication>'
