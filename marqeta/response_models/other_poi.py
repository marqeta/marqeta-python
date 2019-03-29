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
        return self.json_response.get('allow', None)

    @property
    def card_presence_required(self):
        return self.json_response.get('card_presence_required', None)

    @property
    def cardholder_presence_required(self):
        return self.json_response.get('cardholder_presence_required', None)

    def __repr__(self):
        return '<Marqeta.response_models.other_poi.OtherPoi>'
