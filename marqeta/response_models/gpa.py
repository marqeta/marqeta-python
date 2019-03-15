from datetime import datetime, date
import json

class Gpa(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'trigger_amount' : self.trigger_amount,
           'reload_amount' : self.reload_amount,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def trigger_amount(self):
        if 'trigger_amount' in self.json_response:
            return self.json_response['trigger_amount']

    @property
    def reload_amount(self):
        if 'reload_amount' in self.json_response:
            return self.json_response['reload_amount']

    def __repr__(self):
         return '<Marqeta.response_models.gpa.Gpa>'