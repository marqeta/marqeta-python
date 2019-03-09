from datetime import datetime

class AdvancedAuthOtherPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def card_presence(self):
        if 'card_presence' in self.json_response:
            return self.json_response['card_presence']

    @property
    def cardholder_presence(self):
        if 'cardholder_presence' in self.json_response:
            return self.json_response['cardholder_presence']

    @property
    def partial_approval_capable(self):
        if 'partial_approval_capable' in self.json_response:
            return self.json_response['partial_approval_capable']

