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
        return self.json_response.get('card_presence', None)

    @property
    def cardholder_presence(self):
        return self.json_response.get('cardholder_presence', None)

    @property
    def partial_approval_capable(self):
        return self.json_response.get('partial_approval_capable', None)

    def __repr__(self):
        return '<Marqeta.response_models.advanced_auth_other_poi.AdvancedAuthOtherPoi>' + self.__str__()
