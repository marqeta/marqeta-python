from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class MonitorResponse(object):

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
    def metadata(self):
        return self.json_response.get('metadata', None)

    @property
    def errors(self):
        return self.json_response.get('errors', None)

    def __repr__(self):
         return '<Marqeta.response_models.monitor_response.MonitorResponse>' + self.__str__()
