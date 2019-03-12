class FileProcessingRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

