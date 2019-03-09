from datetime import datetime
from marqeta.response_models.funding_source_model import FundingSourceModel

class BankAccountFundingSourceModel(FundingSourceModel):

    def __init__(self, json_response):
        self.json_response = json_response

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

