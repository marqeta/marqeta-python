from datetime import datetime

class CampaignUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
            return self.json_response['start_date']

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return self.json_response['end_date']

    @property
    def store_tokens(self):
        if 'store_tokens' in self.json_response:
            return self.json_response['store_tokens']

