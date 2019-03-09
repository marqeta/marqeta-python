from datetime import datetime

class GatewayProgramVersionUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def version(self):
        if 'version' in self.json_response:
            return self.json_response['version']

