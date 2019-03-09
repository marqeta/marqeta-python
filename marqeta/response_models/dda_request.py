from datetime import datetime

class DdaRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def dda(self):
        if 'dda' in self.json_response:
            return self.json_response['dda']

