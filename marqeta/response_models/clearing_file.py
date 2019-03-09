from datetime import datetime

class ClearingFile(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def file(self):
        if 'file' in self.json_response:
            return self.json_response['file']

