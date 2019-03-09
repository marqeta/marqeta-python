from datetime import datetime

class AuthControlExemptMidsUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

