from datetime import datetime

class MerchantScope(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def mcc(self):
        if 'mcc' in self.json_response:
            return self.json_response['mcc']

    @property
    def mcc_group(self):
        if 'mcc_group' in self.json_response:
            return self.json_response['mcc_group']

