from datetime import datetime, date
import json

class FulfillmentAddressRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'first_name' : self.first_name,
           'middle_name' : self.middle_name,
           'last_name' : self.last_name,
           'address1' : self.address1,
           'address2' : self.address2,
           'city' : self.city,
           'state' : self.state,
           'zip' : self.zip,
           'country' : self.country,
           'phone' : self.phone,
           'postal_code' : self.postal_code,
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
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    def __repr__(self):
         return '<Marqeta.response_models.fulfillment_address_request.FulfillmentAddressRequest>'