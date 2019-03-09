from datetime import datetime

class AvsControlOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def validate(self):
        if 'validate' in self.json_response:
            return self.json_response['validate']

    @property
    def decline_on_address_number_mismatch(self):
        if 'decline_on_address_number_mismatch' in self.json_response:
            return self.json_response['decline_on_address_number_mismatch']

    @property
    def decline_on_postal_code_mismatch(self):
        if 'decline_on_postal_code_mismatch' in self.json_response:
            return self.json_response['decline_on_postal_code_mismatch']

