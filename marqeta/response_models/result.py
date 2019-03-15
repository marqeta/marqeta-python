from datetime import datetime, date
from marqeta.response_models.result_code import ResultCode
import json

class Result(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'status' : self.status,
           'codes' : self.codes,
           'failed_questions_count' : self.failed_questions_count,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

    @property
    def codes(self):
        if 'codes' in self.json_response:
            return [ResultCode(val) for val in self.json_response['codes']]

    @property
    def failed_questions_count(self):
        if 'failed_questions_count' in self.json_response:
            return self.json_response['failed_questions_count']

    def __repr__(self):
         return '<Marqeta.response_models.result.Result>'