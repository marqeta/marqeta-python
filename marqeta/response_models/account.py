from datetime import datetime, date
import json

class Account(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'id' : self.id,
           'email_address' : self.email_address,
           'score' : self.score,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def email_address(self):
        if 'email_address' in self.json_response:
            return self.json_response['email_address']

    @property
    def score(self):
        if 'score' in self.json_response:
            return self.json_response['score']

    def __repr__(self):
         return '<Marqeta.response_models.account.Account>'