from datetime import datetime

class RealTimeFeeGroupRequest(object):

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
    def fee_tokens(self):
        if 'fee_tokens' in self.json_response:
            return self.json_response['fee_tokens']

