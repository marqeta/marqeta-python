from datetime import datetime, date
import json


class SelectiveAuth(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def sa_mode(self):
        return self.json_response.get('sa_mode', None)

    @property
    def enable_regex_search_chain(self):
        return self.json_response.get('enable_regex_search_chain', None)

    @property
    def dmd_location_sensitivity(self):
        return self.json_response.get('dmd_location_sensitivity', None)

    def __repr__(self):
        return '<Marqeta.response_models.selective_auth.SelectiveAuth>'
