from datetime import datetime, date
import json

class MerchantUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def contact(self):
        if 'contact' in self.json_response:
            return self.json_response['contact']

    @property
    def contact_email(self):
        if 'contact_email' in self.json_response:
            return self.json_response['contact_email']

    @property
    def longitude(self):
        if 'longitude' in self.json_response:
            return self.json_response['longitude']

    @property
    def latitude(self):
        if 'latitude' in self.json_response:
            return self.json_response['latitude']

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
    def province(self):
        if 'province' in self.json_response:
            return self.json_response['province']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def partial_auth_flag(self):
        if 'partial_auth_flag' in self.json_response:
            return self.json_response['partial_auth_flag']

    def __repr__(self):
         return '<Marqeta.response_models.merchant_update_model.MerchantUpdateModel>'