from datetime import datetime, date
from marqeta.response_models.result_code import ResultCode
import json


class Result(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def status(self):

        return self.json_response.get('status', None)

    @property
    def codes(self):

        if 'codes' in self.json_response:
            return [ResultCode(val) for val in self.json_response['codes']]

    @property
    def failed_questions_count(self):

        return self.json_response.get('failed_questions_count', None)

    def __repr__(self):
        return '<Marqeta.response_models.result.Result>'
