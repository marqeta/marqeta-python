from datetime import datetime

class RealTimeStandinCriteria(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

