from datetime import datetime
from marqeta.response_models.clearing_file import ClearingFile

class ClearingFileResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def clearing_files(self):
        if 'clearing_files' in self.json_response:
            return [ClearingFile(val) for val in self.json_response['clearing_files']]

