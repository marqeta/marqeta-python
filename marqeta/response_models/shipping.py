from datetime import datetime, date
from marqeta.response_models.fulfillment_address_request import FulfillmentAddressRequest
from marqeta.response_models.fulfillment_address_request import FulfillmentAddressRequest
import json


class Shipping(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def method(self):

        return self.json_response.get('method', None)

    @property
    def return_address(self):

        if 'return_address' in self.json_response:
            return FulfillmentAddressRequest(self.json_response['return_address'])

    @property
    def recipient_address(self):

        if 'recipient_address' in self.json_response:
            return FulfillmentAddressRequest(self.json_response['recipient_address'])

    @property
    def care_of_line(self):

        return self.json_response.get('care_of_line', None)

    def __repr__(self):
        return '<Marqeta.response_models.shipping.Shipping>'
