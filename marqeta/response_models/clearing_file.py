from datetime import datetime, date
import json

class ClearingFile(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'network' : self.network,
           'file' : self.file,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def file(self):
        if 'file' in self.json_response:
            return self.json_response['file']

    def __repr__(self):
         return '<Marqeta.response_models.clearing_file.ClearingFile>'