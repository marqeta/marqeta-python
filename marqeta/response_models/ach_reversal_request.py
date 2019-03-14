from datetime import datetime, date
import json

class AchReversalRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'reason_code' : self.reason_code,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    def __repr__(self):
         return '<Marqeta.response_models.ach_reversal_request.AchReversalRequest>'