from datetime import datetime
from marqeta.response_models.clearing_record_request_model import ClearingRecordRequestModel

class ClearingFileRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transaction_tokens(self):
        if 'transaction_tokens' in self.json_response:
            return [ClearingRecordRequestModel(val) for val in self.json_response['transaction_tokens']]

    @property
    def wait_timeout(self):
        if 'wait_timeout' in self.json_response:
            return self.json_response['wait_timeout']

    @property
    def batch_id(self):
        if 'batch_id' in self.json_response:
            return self.json_response['batch_id']

    @property
    def clearing_folder(self):
        if 'clearing_folder' in self.json_response:
            return self.json_response['clearing_folder']

    @property
    def encrypt_file(self):
        if 'encrypt_file' in self.json_response:
            return self.json_response['encrypt_file']

    @property
    def create_completion_file(self):
        if 'create_completion_file' in self.json_response:
            return self.json_response['create_completion_file']

