from datetime import datetime

class SelectiveAuth(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

