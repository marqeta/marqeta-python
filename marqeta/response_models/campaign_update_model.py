from datetime import datetime, date
import json

class CampaignUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'active' : self.active,
           'start_date' : self.start_date,
           'end_date' : self.end_date,
           'store_tokens' : self.store_tokens,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.campaign_update_model.CampaignUpdateModel>'