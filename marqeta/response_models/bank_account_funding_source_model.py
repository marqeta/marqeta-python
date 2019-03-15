from datetime import datetime, date
from marqeta.response_models.funding_source_model import FundingSourceModel
import json

class BankAccountFundingSourceModel(FundingSourceModel):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'account_suffix' : self.account_suffix,
           'account_type' : self.account_type,
           'name_on_account' : self.name_on_account,
           'routing_number' : self.routing_number,
           'verification_status' : self.verification_status,
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
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def account_suffix(self):
        if 'account_suffix' in self.json_response:
            return self.json_response['account_suffix']

    @property
    def account_type(self):
        if 'account_type' in self.json_response:
            return self.json_response['account_type']

    @property
    def name_on_account(self):
        if 'name_on_account' in self.json_response:
            return self.json_response['name_on_account']

    @property
    def routing_number(self):
        if 'routing_number' in self.json_response:
            return self.json_response['routing_number']

    @property
    def verification_status(self):
        if 'verification_status' in self.json_response:
            return self.json_response['verification_status']

    def __repr__(self):
         return '<Marqeta.response_models.bank_account_funding_source_model.BankAccountFundingSourceModel>'