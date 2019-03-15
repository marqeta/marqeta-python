from datetime import datetime, date
import json

class PasswordUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'new_password' : self.new_password,
           'current_password' : self.current_password,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def new_password(self):
        if 'new_password' in self.json_response:
            return self.json_response['new_password']

    @property
    def current_password(self):
        if 'current_password' in self.json_response:
            return self.json_response['current_password']

    def __repr__(self):
         return '<Marqeta.response_models.password_update_model.PasswordUpdateModel>'