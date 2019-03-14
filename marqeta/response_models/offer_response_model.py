from datetime import datetime, date
import json

class OfferResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'active' : self.active,
           'name' : self.name,
           'start_date' : self.start_date,
           'end_date' : self.end_date,
           'purchase_amount' : self.purchase_amount,
           'reward_amount' : self.reward_amount,
           'reward_trigger_amount' : self.reward_trigger_amount,
           'campaign_token' : self.campaign_token,
           'currency_code' : self.currency_code,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
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
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
                return datetime.strptime(self.json_response['start_date'], '%Y-%m-%d').date()

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
                return datetime.strptime(self.json_response['end_date'], '%Y-%m-%d').date()

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
    def campaign_token(self):
        if 'campaign_token' in self.json_response:
            return self.json_response['campaign_token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
         return '<Marqeta.response_models.offer_response_model.OfferResponseModel>'