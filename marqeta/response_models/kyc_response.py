from datetime import datetime, date
from marqeta.response_models.result import Result
from marqeta.response_models.kyc_question import KycQuestion
import json

class KycResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'token' : self.token,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'result' : self.result,
           'manual_override' : self.manual_override,
           'notes' : self.notes,
           'questions' : self.questions,
           'reference_id' : self.reference_id,
         }
        return json.dumps(dict, default=self.json_serial)

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
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def result(self):
        if 'result' in self.json_response:
            return Result(self.json_response['result'])

    @property
    def manual_override(self):
        if 'manual_override' in self.json_response:
            return self.json_response['manual_override']

    @property
    def notes(self):
        if 'notes' in self.json_response:
            return self.json_response['notes']

    @property
    def questions(self):
        if 'questions' in self.json_response:
            return [KycQuestion(val) for val in self.json_response['questions']]

    @property
    def reference_id(self):
        if 'reference_id' in self.json_response:
            return self.json_response['reference_id']

    def __repr__(self):
         return '<Marqeta.response_models.kyc_response.KycResponse>'