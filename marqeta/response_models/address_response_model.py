from datetime import datetime, date
import json

class AddressResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'address1' : self.address1,
           'address2' : self.address2,
           'city' : self.city,
           'state' : self.state,
           'zip' : self.zip,
           'postal_code' : self.postal_code,
           'country' : self.country,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def address1(self):
        if 'address1' in self.json_response:
            return self.json_response['address1']

    @property
    def address2(self):
        if 'address2' in self.json_response:
            return self.json_response['address2']

    @property
    def city(self):
        if 'city' in self.json_response:
            return self.json_response['city']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    def __repr__(self):
         return '<Marqeta.response_models.address_response_model.AddressResponseModel>'