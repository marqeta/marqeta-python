from datetime import datetime, date
import json


class IdentificationResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def value(self):
        return self.json_response.get('value', None)

    @property
    def expiration_date(self):
        if 'expiration_date' in self.json_response:
            return datetime.strptime(self.json_response['expiration_date'], '%Y-%m-%d').date()

    def __repr__(self):
        return '<Marqeta.response_models.identification_response_model.IdentificationResponseModel>'
