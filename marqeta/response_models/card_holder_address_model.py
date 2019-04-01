from datetime import datetime, date
import json


class CardHolderAddressModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def first_name(self):
        return self.json_response.get('first_name', None)

    @property
    def last_name(self):
        return self.json_response.get('last_name', None)

    @property
    def address_1(self):
        return self.json_response.get('address_1', None)

    @property
    def address_2(self):
        return self.json_response.get('address_2', None)

    @property
    def city(self):
        return self.json_response.get('city', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def zip(self):
        return self.json_response.get('zip', None)

    @property
    def country(self):
        return self.json_response.get('country', None)

    @property
    def phone(self):
        return self.json_response.get('phone', None)

    @property
    def is_default_address(self):
        return self.json_response.get('is_default_address', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def postal_code(self):
        return self.json_response.get('postal_code', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_holder_address_model.CardHolderAddressModel>' + self.__str__()
