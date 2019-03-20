from datetime import datetime, date
import json

class HealthCheckResult(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.health_check_result.HealthCheckResult>'