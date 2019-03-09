from datetime import datetime

class Airline(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def passenger_name(self):
        if 'passenger_name' in self.json_response:
            return self.json_response['passenger_name']

    @property
    def depart_date(self):
        if 'depart_date' in self.json_response:
            return datetime.strptime(self.json_response['depart_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def origination_city(self):
        if 'origination_city' in self.json_response:
            return self.json_response['origination_city']

