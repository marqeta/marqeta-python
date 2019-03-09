from datetime import datetime

class HealthCheckResult(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def component(self):
        if 'component' in self.json_response:
            return self.json_response['component']

    @property
    def healthy(self):
        if 'healthy' in self.json_response:
            return self.json_response['healthy']

    @property
    def fatal(self):
        if 'fatal' in self.json_response:
            return self.json_response['fatal']

    @property
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

