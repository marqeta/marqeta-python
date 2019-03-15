from datetime import datetime, date
import json

class DdaRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'dda' : self.dda,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def dda(self):
        if 'dda' in self.json_response:
            return self.json_response['dda']

    def __repr__(self):
         return '<Marqeta.response_models.dda_request.DdaRequest>'