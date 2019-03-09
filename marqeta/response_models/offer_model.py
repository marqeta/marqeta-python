from datetime import datetime

class OfferModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

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
            return datetime.strptime(self.json_response['start_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return datetime.strptime(self.json_response['end_date'], '%Y-%m-%dT%H:%M:%SZ')

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

