from datetime import datetime, date
from marqeta.response_models.real_time_fee_assessment_request import RealTimeFeeAssessmentRequest
import json

class FeeRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'amount' : self.amount,
           'tags' : self.tags,
           'token' : self.token,
           'currency_code' : self.currency_code,
           'active' : self.active,
           'real_time_assessment' : self.real_time_assessment,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

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

    def __repr__(self):
         return '<Marqeta.response_models.fee_request.FeeRequest>'