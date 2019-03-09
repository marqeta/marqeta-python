from datetime import datetime

class EchoPingResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def success(self):
        if 'success' in self.json_response:
            return self.json_response['success']

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def payload(self):
        if 'payload' in self.json_response:
            return self.json_response['payload']

