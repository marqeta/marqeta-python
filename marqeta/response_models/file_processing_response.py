from datetime import datetime, date
import json

class FileProcessingResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'token' : self.token,
           'file_process_type' : self.file_process_type,
           'source_file' : self.source_file,
           'archive_file' : self.archive_file,
           'file_process_status' : self.file_process_status,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

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

    @property
    def file_process_status(self):
        if 'file_process_status' in self.json_response:
            return self.json_response['file_process_status']

    def __repr__(self):
         return '<Marqeta.response_models.file_processing_response.FileProcessingResponse>'