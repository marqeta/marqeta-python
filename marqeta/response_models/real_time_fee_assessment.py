from datetime import datetime

class RealTimeFeeAssessment(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

