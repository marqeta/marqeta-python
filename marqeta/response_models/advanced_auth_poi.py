from datetime import datetime
from marqeta.response_models.advanced_auth_other_poi import AdvancedAuthOtherPoi

class AdvancedAuthPoi(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

