from datetime import datetime

class MsaOrderUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
            return datetime.strptime(self.json_response['start_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return datetime.strptime(self.json_response['end_date'], '%Y-%m-%dT%H:%M:%SZ')

