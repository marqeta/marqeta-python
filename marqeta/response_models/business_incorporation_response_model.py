from datetime import datetime
from marqeta.response_models.address_response_model import AddressResponseModel

class BusinessIncorporationResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

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
            return AddressResponseModel(self.json_response['address_registered_under'])

    @property
    def incorporation_type(self):
        if 'incorporation_type' in self.json_response:
            return self.json_response['incorporation_type']

