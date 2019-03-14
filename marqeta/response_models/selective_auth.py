from datetime import datetime, date
import json

class SelectiveAuth(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'sa_mode' : self.sa_mode,
           'enable_regex_search_chain' : self.enable_regex_search_chain,
           'dmd_location_sensitivity' : self.dmd_location_sensitivity,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def sa_mode(self):
        if 'sa_mode' in self.json_response:
            return self.json_response['sa_mode']

    @property
    def enable_regex_search_chain(self):
        if 'enable_regex_search_chain' in self.json_response:
            return self.json_response['enable_regex_search_chain']

    @property
    def dmd_location_sensitivity(self):
        if 'dmd_location_sensitivity' in self.json_response:
            return self.json_response['dmd_location_sensitivity']

    def __repr__(self):
         return '<Marqeta.response_models.selective_auth.SelectiveAuth>'