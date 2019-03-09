from datetime import datetime

class TerminalModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def tid(self):
        if 'tid' in self.json_response:
            return self.json_response['tid']

    @property
    def partial_approval_capable(self):
        if 'partial_approval_capable' in self.json_response:
            return self.json_response['partial_approval_capable']

    @property
    def cardholder_presence(self):
        if 'cardholder_presence' in self.json_response:
            return self.json_response['cardholder_presence']

    @property
    def card_presence(self):
        if 'card_presence' in self.json_response:
            return self.json_response['card_presence']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def processing_type(self):
        if 'processing_type' in self.json_response:
            return self.json_response['processing_type']

    @property
    def pin_present(self):
        if 'pin_present' in self.json_response:
            return self.json_response['pin_present']

