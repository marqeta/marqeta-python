from datetime import datetime

class Application(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def program(self):
        if 'program' in self.json_response:
            return self.json_response['program']

    @property
    def environment(self):
        if 'environment' in self.json_response:
            return self.json_response['environment']

    @property
    def program_short_code(self):
        if 'program_short_code' in self.json_response:
            return self.json_response['program_short_code']

    @property
    def client_api_base_url(self):
        if 'client_api_base_url' in self.json_response:
            return self.json_response['client_api_base_url']

    @property
    def assets_url(self):
        if 'assets_url' in self.json_response:
            return self.json_response['assets_url']

    @property
    def access_code(self):
        if 'access_code' in self.json_response:
            return self.json_response['access_code']

