from datetime import datetime, date
from marqeta.response_models.gpa import Gpa
from marqeta.response_models.msa import Msa
import json

class OrderScope(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'gpa' : self.gpa,
           'msa' : self.msa,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def gpa(self):
        if 'gpa' in self.json_response:
            return Gpa(self.json_response['gpa'])

    @property
    def msa(self):
        if 'msa' in self.json_response:
            return Msa(self.json_response['msa'])

    def __repr__(self):
         return '<Marqeta.response_models.order_scope.OrderScope>'