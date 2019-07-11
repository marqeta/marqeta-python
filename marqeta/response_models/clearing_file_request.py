from datetime import datetime, date
from marqeta.response_models.clearing_record_request_model import ClearingRecordRequestModel
from marqeta.response_models import datetime_object
import json
import re

class ClearingFileRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_tokens(self):
        if 'transaction_tokens' in self.json_response:
            return [ClearingRecordRequestModel(val) for val in self.json_response['transaction_tokens']]

    @property
    def wait_timeout(self):
        return self.json_response.get('wait_timeout', None)

    @property
    def batch_id(self):
        return self.json_response.get('batch_id', None)


    @property
    def clearing_folder(self):
        return self.json_response.get('clearing_folder', None)


    @property
    def encrypt_file(self):
        return self.json_response.get('encrypt_file', None)

    @property
    def create_completion_file(self):
        return self.json_response.get('create_completion_file', None)

    def __repr__(self):
         return '<Marqeta.response_models.clearing_file_request.ClearingFileRequest>' + self.__str__()
