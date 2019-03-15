from datetime import datetime, date
import json

class Airline(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'passenger_name' : self.passenger_name,
           'depart_date' : self.depart_date,
           'origination_city' : self.origination_city,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def passenger_name(self):
        if 'passenger_name' in self.json_response:
            return self.json_response['passenger_name']

    @property
    def depart_date(self):
        if 'depart_date' in self.json_response:
                return datetime.strptime(self.json_response['depart_date'], '%Y-%m-%d').date()

    @property
    def origination_city(self):
        if 'origination_city' in self.json_response:
            return self.json_response['origination_city']

    def __repr__(self):
         return '<Marqeta.response_models.airline.Airline>'