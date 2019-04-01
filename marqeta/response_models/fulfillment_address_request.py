from datetime import datetime, date
import json


class FulfillmentAddressRequest(object):

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
    def middle_name(self):
        return self.json_response.get('middle_name', None)

    @property
    def last_name(self):
        return self.json_response.get('last_name', None)

    @property
    def address1(self):
        return self.json_response.get('address1', None)

    @property
    def address2(self):
        return self.json_response.get('address2', None)

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
    def postal_code(self):
        return self.json_response.get('postal_code', None)

    def __repr__(self):
        return '<Marqeta.response_models.fulfillment_address_request.FulfillmentAddressRequest>' + self.__str__()
