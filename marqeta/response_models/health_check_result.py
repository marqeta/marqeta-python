from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


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
        return self.json_response.get("component", None)

    @property
    def healthy(self):
        return self.json_response.get("healthy", None)

    @property
    def fatal(self):
        return self.json_response.get("fatal", None)

    @property
    def status(self):
        return self.json_response.get("status", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.health_check_result.HealthCheckResult>"
            + self.__str__()
        )
