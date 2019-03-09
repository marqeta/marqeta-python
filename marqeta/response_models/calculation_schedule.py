from datetime import datetime

class CalculationSchedule(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

