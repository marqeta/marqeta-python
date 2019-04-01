from datetime import datetime, date
from marqeta.response_models.real_time_fee_assessment_request import RealTimeFeeAssessmentRequest
import json


class FeeUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get('name', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def tags(self):
        return self.json_response.get('tags', None)

    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def real_time_assessment(self):
        if 'real_time_assessment' in self.json_response:
            return RealTimeFeeAssessmentRequest(self.json_response['real_time_assessment'])

    def __repr__(self):
        return '<Marqeta.response_models.fee_update_request.FeeUpdateRequest>'
