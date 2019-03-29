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
        return self.json_response.get('validate', None)

    @property
    def decline_on_address_number_mismatch(self):
        return self.json_response.get('decline_on_address_number_mismatch', None)

    @property
    def decline_on_postal_code_mismatch(self):
        return self.json_response.get('decline_on_postal_code_mismatch', None)

    def __repr__(self):
        return '<Marqeta.response_models.avs_control_options.AvsControlOptions>'
