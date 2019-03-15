from datetime import datetime, date
import json

class AchModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'account_number' : self.account_number,
           'routing_number' : self.routing_number,
           'name_on_account' : self.name_on_account,
           'account_type' : self.account_type,
           'verification_override' : self.verification_override,
           'verification_notes' : self.verification_notes,
           'is_default_account' : self.is_default_account,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def account_number(self):
        if 'account_number' in self.json_response:
            return self.json_response['account_number']

    @property
    def routing_number(self):
        if 'routing_number' in self.json_response:
            return self.json_response['routing_number']

    @property
    def name_on_account(self):
        if 'name_on_account' in self.json_response:
            return self.json_response['name_on_account']

    @property
    def account_type(self):
        if 'account_type' in self.json_response:
            return self.json_response['account_type']

    @property
    def verification_override(self):
        if 'verification_override' in self.json_response:
            return self.json_response['verification_override']

    @property
    def verification_notes(self):
        if 'verification_notes' in self.json_response:
            return self.json_response['verification_notes']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.json_response:
            return self.json_response['is_default_account']

    def __repr__(self):
         return '<Marqeta.response_models.ach_model.AchModel>'