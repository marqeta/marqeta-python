from datetime import datetime
from marqeta.response_models.real_time_fee_assessment_request import RealTimeFeeAssessmentRequest

class FeeUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def real_time_assessment(self):
        if 'real_time_assessment' in self.json_response:
            return RealTimeFeeAssessmentRequest(self.json_response['real_time_assessment'])

