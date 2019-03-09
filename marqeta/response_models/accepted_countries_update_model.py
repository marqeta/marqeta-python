from datetime import datetime

class AcceptedCountriesUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def is_whitelist(self):
        if 'is_whitelist' in self.json_response:
            return self.json_response['is_whitelist']

    @property
    def country_codes(self):
        if 'country_codes' in self.json_response:
            return self.json_response['country_codes']

