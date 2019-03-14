from datetime import datetime, date
import json

class FileProcessingRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'file_process_type' : self.file_process_type,
           'source_file' : self.source_file,
           'archive_file' : self.archive_file,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def file_process_type(self):
        if 'file_process_type' in self.json_response:
            return self.json_response['file_process_type']

    @property
    def source_file(self):
        if 'source_file' in self.json_response:
            return self.json_response['source_file']

    @property
    def archive_file(self):
        if 'archive_file' in self.json_response:
            return self.json_response['archive_file']

    def __repr__(self):
         return '<Marqeta.response_models.file_processing_request.FileProcessingRequest>'