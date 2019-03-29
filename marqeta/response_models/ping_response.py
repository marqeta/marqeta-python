from datetime import datetime, date
from marqeta.response_models.health_check_result import HealthCheckResult
import json


class PingResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def success(self):

        return self.json_response.get('success', None)

    @property
    def version(self):

        return self.json_response.get('version', None)

    @property
    def revision(self):

        return self.json_response.get('revision', None)

    @property
    def timestamp(self):

        return self.json_response.get('timestamp', None)

    @property
    def env(self):

        return self.json_response.get('env', None)

    @property
    def id(self):

        return self.json_response.get('id', None)

    @property
    def system_components(self):

        if 'system_components' in self.json_response:
            return [HealthCheckResult(val) for val in self.json_response['system_components']]

    def __repr__(self):
        return '<Marqeta.response_models.ping_response.PingResponse>'
