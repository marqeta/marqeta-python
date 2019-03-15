from datetime import datetime, date
import json

class MonitorResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'success' : self.success,
           'metadata' : self.metadata,
           'errors' : self.errors,
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
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    @property
    def errors(self):
        if 'errors' in self.json_response:
            return self.json_response['errors']

    def __repr__(self):
         return '<Marqeta.response_models.monitor_response.MonitorResponse>'