from datetime import datetime, date
from marqeta.response_models.address_request_model import AddressRequestModel
from marqeta.response_models.identification_request_model import IdentificationRequestModel
import json

class BusinessProprietorRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'first_name' : self.first_name,
           'middle_name' : self.middle_name,
           'last_name' : self.last_name,
           'alternative_names' : self.alternative_names,
           'title' : self.title,
           'home' : self.home,
           'ssn' : self.ssn,
           'dob' : self.dob,
           'phone' : self.phone,
           'email' : self.email,
           'identifications' : self.identifications,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def first_name(self):
        if 'first_name' in self.json_response:
            return self.json_response['first_name']

    @property
    def middle_name(self):
        if 'middle_name' in self.json_response:
            return self.json_response['middle_name']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def alternative_names(self):
        if 'alternative_names' in self.json_response:
            return self.json_response['alternative_names']

    @property
    def title(self):
        if 'title' in self.json_response:
            return self.json_response['title']

    @property
    def home(self):
        if 'home' in self.json_response:
            return AddressRequestModel(self.json_response['home'])

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

    @property
    def dob(self):
        if 'dob' in self.json_response:
                return datetime.strptime(self.json_response['dob'], '%Y-%m-%d').date()

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

    @property
    def identifications(self):
        if 'identifications' in self.json_response:
            return [IdentificationRequestModel(val) for val in self.json_response['identifications']]

    def __repr__(self):
         return '<Marqeta.response_models.business_proprietor_request_model.BusinessProprietorRequestModel>'