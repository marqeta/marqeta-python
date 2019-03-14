from datetime import datetime, date
from marqeta.response_models.address_request_model import AddressRequestModel
import json

class BusinessIncorporationRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'is_public' : self.is_public,
           'stock_symbol' : self.stock_symbol,
           'state_of_incorporation' : self.state_of_incorporation,
           'name_registered_under' : self.name_registered_under,
           'address_registered_under' : self.address_registered_under,
           'incorporation_type' : self.incorporation_type,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def is_public(self):
        if 'is_public' in self.json_response:
            return self.json_response['is_public']

    @property
    def stock_symbol(self):
        if 'stock_symbol' in self.json_response:
            return self.json_response['stock_symbol']

    @property
    def state_of_incorporation(self):
        if 'state_of_incorporation' in self.json_response:
            return self.json_response['state_of_incorporation']

    @property
    def name_registered_under(self):
        if 'name_registered_under' in self.json_response:
            return self.json_response['name_registered_under']

    @property
    def address_registered_under(self):
        if 'address_registered_under' in self.json_response:
            return AddressRequestModel(self.json_response['address_registered_under'])

    @property
    def incorporation_type(self):
        if 'incorporation_type' in self.json_response:
            return self.json_response['incorporation_type']

    def __repr__(self):
         return '<Marqeta.response_models.business_incorporation_request_model.BusinessIncorporationRequestModel>'