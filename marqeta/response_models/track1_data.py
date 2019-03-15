from datetime import datetime, date
import json

class Track1Data(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'cvv' : self.cvv,
           'atc' : self.atc,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def cvv(self):
        if 'cvv' in self.json_response:
            return self.json_response['cvv']

    @property
    def atc(self):
        if 'atc' in self.json_response:
            return self.json_response['atc']

    def __repr__(self):
         return '<Marqeta.response_models.track1_data.Track1Data>'