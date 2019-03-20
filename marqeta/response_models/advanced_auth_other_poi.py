from datetime import datetime, date
import json

class AdvancedAuthOtherPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.advanced_auth_other_poi.AdvancedAuthOtherPoi>'