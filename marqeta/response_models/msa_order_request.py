from datetime import datetime, date
import json

class MsaOrderRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'campaign_token' : self.campaign_token,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'currency_code' : self.currency_code,
           'purchase_amount' : self.purchase_amount,
           'reward_amount' : self.reward_amount,
           'reward_trigger_amount' : self.reward_trigger_amount,
           'start_date' : self.start_date,
           'end_date' : self.end_date,
           'funding_source_token' : self.funding_source_token,
           'funding_source_address_token' : self.funding_source_address_token,
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
    def campaign_token(self):
        if 'campaign_token' in self.json_response:
            return self.json_response['campaign_token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def purchase_amount(self):
        if 'purchase_amount' in self.json_response:
            return self.json_response['purchase_amount']

    @property
    def reward_amount(self):
        if 'reward_amount' in self.json_response:
            return self.json_response['reward_amount']

    @property
    def reward_trigger_amount(self):
        if 'reward_trigger_amount' in self.json_response:
            return self.json_response['reward_trigger_amount']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
                return datetime.strptime(self.json_response['start_date'], '%Y-%m-%d').date()

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
                return datetime.strptime(self.json_response['end_date'], '%Y-%m-%d').date()

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.json_response:
            return self.json_response['funding_source_token']

    @property
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.json_response:
            return self.json_response['funding_source_address_token']

    def __repr__(self):
         return '<Marqeta.response_models.msa_order_request.MsaOrderRequest>'