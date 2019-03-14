from datetime import datetime, date
from marqeta.response_models.advanced_auth_other_poi import AdvancedAuthOtherPoi
import json

class AdvancedAuthPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'other' : self.other,
           'ecommerce' : self.ecommerce,
           'atm' : self.atm,
         }
        return json.dumps(dict, default=self.json_serial)

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
        if 'ecommerce' in self.json_response:
            return self.json_response['ecommerce']

    @property
    def atm(self):
        if 'atm' in self.json_response:
            return self.json_response['atm']

    def __repr__(self):
         return '<Marqeta.response_models.advanced_auth_poi.AdvancedAuthPoi>'