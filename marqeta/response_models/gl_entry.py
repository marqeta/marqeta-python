from datetime import datetime

class GlEntry(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def detail(self):
        if 'detail' in self.json_response:
            return self.json_response['detail']

    @property
    def tag(self):
        if 'tag' in self.json_response:
            return self.json_response['tag']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def layer(self):
        if 'layer' in self.json_response:
            return self.json_response['layer']

    @property
    def account(self):
        if 'account' in self.json_response:
            return self.json_response['account']

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

