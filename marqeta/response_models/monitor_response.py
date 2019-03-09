from datetime import datetime

class MonitorResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def success(self):
        if 'success' in self.json_response:
            return self.json_response['success']

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    @property
    def errors(self):
        if 'errors' in self.json_response:
            return self.json_response['errors']

