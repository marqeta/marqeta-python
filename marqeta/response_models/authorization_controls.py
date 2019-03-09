from datetime import datetime
from marqeta.response_models.hold_increase import HoldIncrease

class AuthorizationControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def hold_increase(self):
        if 'hold_increase' in self.json_response:
            return HoldIncrease(self.json_response['hold_increase'])

    @property
    def hold_expiration_days(self):
        if 'hold_expiration_days' in self.json_response:
            return self.json_response['hold_expiration_days']

