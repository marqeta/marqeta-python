from datetime import datetime, date
from marqeta.response_models.result import Result
from marqeta.response_models.kyc_question import KycQuestion
import json


class KycResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):

        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):

        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token(self):

        return self.json_response.get('token', None)

    @property
    def user_token(self):

        return self.json_response.get('user_token', None)

    @property
    def business_token(self):

        return self.json_response.get('business_token', None)

    @property
    def result(self):

        if 'result' in self.json_response:
            return Result(self.json_response['result'])

    @property
    def manual_override(self):

        return self.json_response.get('manual_override', None)

    @property
    def notes(self):

        return self.json_response.get('notes', None)

    @property
    def questions(self):

        if 'questions' in self.json_response:
            return [KycQuestion(val) for val in self.json_response['questions']]

    @property
    def reference_id(self):

        return self.json_response.get('reference_id', None)

    def __repr__(self):
        return '<Marqeta.response_models.kyc_response.KycResponse>'
