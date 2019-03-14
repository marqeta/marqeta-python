from datetime import datetime, date
from marqeta.response_models.clearing_file import ClearingFile
import json

class ClearingFileResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'clearing_files' : self.clearing_files,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def clearing_files(self):
        if 'clearing_files' in self.json_response:
            return [ClearingFile(val) for val in self.json_response['clearing_files']]

    def __repr__(self):
         return '<Marqeta.response_models.clearing_file_response.ClearingFileResponse>'