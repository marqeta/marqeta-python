from datetime import datetime, date
from marqeta.response_models.real_time_fee_assessment import RealTimeFeeAssessment
import json


class Fee(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

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
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)

    @property
    def real_time_assessment(self):
        if 'real_time_assessment' in self.json_response:
            return RealTimeFeeAssessment(self.json_response['real_time_assessment'])

    def __repr__(self):
        return '<Marqeta.response_models.fee.Fee>'
