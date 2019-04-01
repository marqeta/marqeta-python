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
        return self.json_response.get('token', None)

    @property
    def value_type(self):
        return self.json_response.get('value_type', None)

    @property
    def name(self):
        return self.json_response.get('name', None)

    @property
    def steps(self):
        return self.json_response.get('steps', None)

    @property
    def step_values(self):
        return self.json_response.get('step_values', None)

    def __repr__(self):
        return '<Marqeta.response_models.calculation_schedule.CalculationSchedule>' + self.__str__()
