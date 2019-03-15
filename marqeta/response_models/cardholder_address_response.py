from datetime import datetime, date
import json

class CardholderAddressResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'token' : self.token,
           'first_name' : self.first_name,
           'last_name' : self.last_name,
           'address_1' : self.address_1,
           'address_2' : self.address_2,
           'city' : self.city,
           'state' : self.state,
           'zip' : self.zip,
           'postal_code' : self.postal_code,
           'country' : self.country,
           'phone' : self.phone,
           'is_default_address' : self.is_default_address,
           'active' : self.active,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def first_name(self):
        if 'first_name' in self.json_response:
            return self.json_response['first_name']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def address_1(self):
        if 'address_1' in self.json_response:
            return self.json_response['address_1']

    @property
    def address_2(self):
        if 'address_2' in self.json_response:
            return self.json_response['address_2']

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

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def is_default_address(self):
        if 'is_default_address' in self.json_response:
            return self.json_response['is_default_address']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
         return '<Marqeta.response_models.cardholder_address_response.CardholderAddressResponse>'