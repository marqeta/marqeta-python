from datetime import datetime


class CardholderAddressResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.response:
            return self.response['business_token']

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def first_name(self):
        if 'first_name' in self.response:
            return self.response['first_name']

    @property
    def last_name(self):
        if 'last_name' in self.response:
            return self.response['last_name']

    @property
    def address_1(self):
        if 'address_1' in self.response:
            return self.response['address_1']

    @property
    def address_2(self):
        if 'address_2' in self.response:
            return self.response['address_2']

    @property
    def city(self):
        if 'city' in self.response:
            return self.response['city']

    @property
    def state(self):
        if 'state' in self.response:
            return self.response['state']

    @property
    def zip(self):
        if 'zip' in self.response:
            return self.response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.response:
            return self.response['postal_code']

    @property
    def country(self):
        if 'country' in self.response:
            return self.response['country']

    @property
    def phone(self):
        if 'phone' in self.response:
            return self.response['phone']

    @property
    def is_default_address(self):
        if 'is_default_address' in self.response:
            return self.response['is_default_address']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')
