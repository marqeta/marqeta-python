from datetime import datetime, date
import json


class LoadVelocityModel(object):

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
    def description(self):
        return self.json_response.get('description', None)

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def layers(self):
        return self.json_response.get('layers', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def days(self):
        return self.json_response.get('days', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    def __repr__(self):
        return '<Marqeta.response_models.load_velocity_model.LoadVelocityModel>' + self.__str__()
