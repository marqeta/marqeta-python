from datetime import datetime, date
import json

class AcceptedCountriesUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.accepted_countries_update_model.AcceptedCountriesUpdateModel>'