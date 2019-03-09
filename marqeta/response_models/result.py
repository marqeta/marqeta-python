from datetime import datetime
from marqeta.response_models.result_code import ResultCode

class Result(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

