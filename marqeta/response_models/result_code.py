from datetime import datetime, date
import json

class ResultCode(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'code' : self.code,
           'message' : self.message,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def code(self):
        if 'code' in self.json_response:
            return self.json_response['code']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

    def __repr__(self):
         return '<Marqeta.response_models.result_code.ResultCode>'