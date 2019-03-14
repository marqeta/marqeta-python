from datetime import datetime, date
import json

class IdentificationResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'type' : self.type,
           'value' : self.value,
           'expiration_date' : self.expiration_date,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

    @property
    def expiration_date(self):
        if 'expiration_date' in self.json_response:
            return self.json_response['expiration_date']

    def __repr__(self):
         return '<Marqeta.response_models.identification_response_model.IdentificationResponseModel>'