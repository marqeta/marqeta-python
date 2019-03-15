from datetime import datetime, date
import json

class RealTimeStandinCriteria(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'enabled' : self.enabled,
           'include_connection_errors' : self.include_connection_errors,
           'include_response_timeouts' : self.include_response_timeouts,
           'include_application_errors' : self.include_application_errors,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def enabled(self):
        if 'enabled' in self.json_response:
            return self.json_response['enabled']

    @property
    def include_connection_errors(self):
        if 'include_connection_errors' in self.json_response:
            return self.json_response['include_connection_errors']

    @property
    def include_response_timeouts(self):
        if 'include_response_timeouts' in self.json_response:
            return self.json_response['include_response_timeouts']

    @property
    def include_application_errors(self):
        if 'include_application_errors' in self.json_response:
            return self.json_response['include_application_errors']

    def __repr__(self):
         return '<Marqeta.response_models.real_time_standin_criteria.RealTimeStandinCriteria>'