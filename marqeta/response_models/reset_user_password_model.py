from datetime import datetime, date
import json

class ResetUserPasswordModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'user_token' : self.user_token,
           'new_password' : self.new_password,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def new_password(self):
        if 'new_password' in self.json_response:
            return self.json_response['new_password']

    def __repr__(self):
         return '<Marqeta.response_models.reset_user_password_model.ResetUserPasswordModel>'