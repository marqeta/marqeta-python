from datetime import datetime, date
import json


class RealTimeStandinCriteria(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def enabled(self):
        return self.json_response.get('enabled', None)

    @property
    def include_connection_errors(self):
        return self.json_response.get('include_connection_errors', None)

    @property
    def include_response_timeouts(self):
        return self.json_response.get('include_response_timeouts', None)

    @property
    def include_application_errors(self):
        return self.json_response.get('include_application_errors', None)

    def __repr__(self):
        return '<Marqeta.response_models.real_time_standin_criteria.RealTimeStandinCriteria>' + self.__str__()
