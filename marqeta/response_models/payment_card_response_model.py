from datetime import datetime, date
import json

class PaymentCardResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'type' : self.type,
           'token' : self.token,
           'account_suffix' : self.account_suffix,
           'account_type' : self.account_type,
           'active' : self.active,
           'is_default_account' : self.is_default_account,
           'exp_date' : self.exp_date,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def account_suffix(self):
        if 'account_suffix' in self.json_response:
            return self.json_response['account_suffix']

    @property
    def account_type(self):
        if 'account_type' in self.json_response:
            return self.json_response['account_type']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.json_response:
            return self.json_response['is_default_account']

    @property
    def exp_date(self):
        if 'exp_date' in self.json_response:
            return self.json_response['exp_date']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    def __repr__(self):
         return '<Marqeta.response_models.payment_card_response_model.PaymentCardResponseModel>'