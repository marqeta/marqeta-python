from datetime import datetime, date
import json

class AvsControlOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.avs_control_options.AvsControlOptions>'