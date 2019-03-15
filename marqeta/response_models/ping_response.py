from datetime import datetime, date
from marqeta.response_models.health_check_result import HealthCheckResult
import json

class PingResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'success' : self.success,
           'version' : self.version,
           'revision' : self.revision,
           'timestamp' : self.timestamp,
           'env' : self.env,
           'id' : self.id,
           'system_components' : self.system_components,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def success(self):
        if 'success' in self.json_response:
            return self.json_response['success']

    @property
    def version(self):
        if 'version' in self.json_response:
            return self.json_response['version']

    @property
    def revision(self):
        if 'revision' in self.json_response:
            return self.json_response['revision']

    @property
    def timestamp(self):
        if 'timestamp' in self.json_response:
            return self.json_response['timestamp']

    @property
    def env(self):
        if 'env' in self.json_response:
            return self.json_response['env']

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def system_components(self):
        if 'system_components' in self.json_response:
            return [HealthCheckResult(val) for val in self.json_response['system_components']]

    def __repr__(self):
         return '<Marqeta.response_models.ping_response.PingResponse>'