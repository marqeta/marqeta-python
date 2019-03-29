from datetime import datetime, date
import json


class BillingAddress(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def first_name(self):
        return self.json_response.get('first_name', None)

    @property
    def last_name(self):
        return self.json_response.get('last_name', None)

    @property
    def address(self):
        return self.json_response.get('address', None)

    @property
    def zip(self):
        return self.json_response.get('zip', None)

    def __repr__(self):
        return '<Marqeta.response_models.billing_address.BillingAddress>'
