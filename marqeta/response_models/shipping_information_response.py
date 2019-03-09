from datetime import datetime
from marqeta.response_models.fulfillment_address_response import FulfillmentAddressResponse
from marqeta.response_models.fulfillment_address_response import FulfillmentAddressResponse

class ShippingInformationResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def method(self):
        if 'method' in self.json_response:
            return self.json_response['method']

    @property
    def return_address(self):
        if 'return_address' in self.json_response:
            return FulfillmentAddressResponse(self.json_response['return_address'])

    @property
    def recipient_address(self):
        if 'recipient_address' in self.json_response:
            return FulfillmentAddressResponse(self.json_response['recipient_address'])

    @property
    def care_of_line(self):
        if 'care_of_line' in self.json_response:
            return self.json_response['care_of_line']

