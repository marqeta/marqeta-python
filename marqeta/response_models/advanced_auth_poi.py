from datetime import datetime, date
from marqeta.response_models.advanced_auth_other_poi import AdvancedAuthOtherPoi
import json


class AdvancedAuthPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def other(self):
        if 'other' in self.json_response:
            return AdvancedAuthOtherPoi(self.json_response['other'])

    @property
    def ecommerce(self):
        return self.json_response.get('ecommerce', None)

    @property
    def atm(self):
        return self.json_response.get('atm', None)

    def __repr__(self):
        return '<Marqeta.response_models.advanced_auth_poi.AdvancedAuthPoi>'
