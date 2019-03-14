from datetime import datetime, date
import json

class ClearingAndSettlement(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'overdraft_destination' : self.overdraft_destination,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def overdraft_destination(self):
        if 'overdraft_destination' in self.json_response:
            return self.json_response['overdraft_destination']

    def __repr__(self):
         return '<Marqeta.response_models.clearing_and_settlement.ClearingAndSettlement>'