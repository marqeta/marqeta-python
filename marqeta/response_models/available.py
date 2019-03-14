from datetime import datetime, date
import json

class Available(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'uses' : self.uses,
           'amount' : self.amount,
           'days_remaining' : self.days_remaining,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def uses(self):
        if 'uses' in self.json_response:
            return self.json_response['uses']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def days_remaining(self):
        if 'days_remaining' in self.json_response:
            return self.json_response['days_remaining']

    def __repr__(self):
         return '<Marqeta.response_models.available.Available>'