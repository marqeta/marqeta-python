from datetime import datetime, date
from marqeta.response_models.address_request_model import AddressRequestModel
from marqeta.response_models import datetime_object
import json
import re

class BusinessIncorporationRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def is_public(self):
        return self.json_response.get('is_public', None)

    @property
    def stock_symbol(self):
        return self.json_response.get('stock_symbol', None)


    @property
    def state_of_incorporation(self):
        return self.json_response.get('state_of_incorporation', None)


    @property
    def name_registered_under(self):
        return self.json_response.get('name_registered_under', None)


    @property
    def address_registered_under(self):
        if 'address_registered_under' in self.json_response:
            return AddressRequestModel(self.json_response['address_registered_under'])

    @property
    def incorporation_type(self):
        return self.json_response.get('incorporation_type', None)


    def __repr__(self):
         return '<Marqeta.response_models.business_incorporation_request_model.BusinessIncorporationRequestModel>' + self.__str__()
