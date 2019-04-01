from datetime import datetime, date
from marqeta.response_models.address_response_model import AddressResponseModel
from marqeta.response_models.identification_response_model import IdentificationResponseModel
import json


class BusinessProprietorResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def first_name(self):
        return self.json_response.get('first_name', None)

    @property
    def middle_name(self):
        return self.json_response.get('middle_name', None)

    @property
    def last_name(self):
        return self.json_response.get('last_name', None)

    @property
    def alternative_names(self):
        return self.json_response.get('alternative_names', None)

    @property
    def title(self):
        return self.json_response.get('title', None)

    @property
    def home(self):
        if 'home' in self.json_response:
            return AddressResponseModel(self.json_response['home'])

    @property
    def ssn(self):
        return self.json_response.get('ssn', None)

    @property
    def dob(self):
        if 'dob' in self.json_response:
            return datetime.strptime(self.json_response['dob'], '%Y-%m-%d').date()

    @property
    def phone(self):
        return self.json_response.get('phone', None)

    @property
    def email(self):
        return self.json_response.get('email', None)

    @property
    def identifications(self):
        if 'identifications' in self.json_response:
            return [IdentificationResponseModel(val) for val in self.json_response['identifications']]

    def __repr__(self):
        return '<Marqeta.response_models.business_proprietor_response_model.BusinessProprietorResponseModel>'
