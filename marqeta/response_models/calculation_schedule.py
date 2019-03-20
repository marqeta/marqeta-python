from datetime import datetime, date
import json

class CalculationSchedule(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def value_type(self):
        if 'value_type' in self.json_response:
            return self.json_response['value_type']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def steps(self):
        if 'steps' in self.json_response:
            return self.json_response['steps']

    @property
    def step_values(self):
        if 'step_values' in self.json_response:
            return self.json_response['step_values']

    def __repr__(self):
         return '<Marqeta.response_models.calculation_schedule.CalculationSchedule>'