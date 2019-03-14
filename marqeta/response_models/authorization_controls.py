from datetime import datetime, date
from marqeta.response_models.hold_increase import HoldIncrease
import json

class AuthorizationControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'hold_increase' : self.hold_increase,
           'hold_expiration_days' : self.hold_expiration_days,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def hold_increase(self):
        if 'hold_increase' in self.json_response:
            return HoldIncrease(self.json_response['hold_increase'])

    @property
    def hold_expiration_days(self):
        if 'hold_expiration_days' in self.json_response:
            return self.json_response['hold_expiration_days']

    def __repr__(self):
         return '<Marqeta.response_models.authorization_controls.AuthorizationControls>'