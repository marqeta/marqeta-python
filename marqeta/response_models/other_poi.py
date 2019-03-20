from datetime import datetime, date
import json

class OtherPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.other_poi.OtherPoi>'