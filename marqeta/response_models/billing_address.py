from datetime import datetime, date
import json

class BillingAddress(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'first_name' : self.first_name,
           'last_name' : self.last_name,
           'address' : self.address,
           'zip' : self.zip,
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
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def address(self):
        if 'address' in self.json_response:
            return self.json_response['address']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    def __repr__(self):
         return '<Marqeta.response_models.billing_address.BillingAddress>'