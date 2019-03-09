from datetime import datetime

class OtherPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def allow(self):
        if 'allow' in self.json_response:
            return self.json_response['allow']

    @property
    def card_presence_required(self):
        if 'card_presence_required' in self.json_response:
            return self.json_response['card_presence_required']

    @property
    def cardholder_presence_required(self):
        if 'cardholder_presence_required' in self.json_response:
            return self.json_response['cardholder_presence_required']

