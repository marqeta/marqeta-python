from datetime import datetime, date
import json

class RealTimeFeeAssessment(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_type(self):
        if 'transaction_type' in self.json_response:
            return self.json_response['transaction_type']

    @property
    def international_enabled(self):
        if 'international_enabled' in self.json_response:
            return self.json_response['international_enabled']

    @property
    def domestic_enabled(self):
        if 'domestic_enabled' in self.json_response:
            return self.json_response['domestic_enabled']

    def __repr__(self):
         return '<Marqeta.response_models.real_time_fee_assessment.RealTimeFeeAssessment>'