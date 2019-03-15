from datetime import datetime, date
from marqeta.response_models.shipping_information_response import ShippingInformationResponse
from marqeta.response_models.card_personalization import CardPersonalization
import json

class CardProductFulfillmentResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'shipping' : self.shipping,
           'card_personalization' : self.card_personalization,
           'payment_instrument' : self.payment_instrument,
           'package_id' : self.package_id,
           'all_zero_card_security_code' : self.all_zero_card_security_code,
           'bin_prefix' : self.bin_prefix,
           'bulk_ship' : self.bulk_ship,
           'pan_length' : self.pan_length,
           'fulfillment_provider' : self.fulfillment_provider,
           'allow_card_creation' : self.allow_card_creation,
           'uppercase_name_lines' : self.uppercase_name_lines,
           'enable_offline_pin' : self.enable_offline_pin,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def shipping(self):
        if 'shipping' in self.json_response:
            return ShippingInformationResponse(self.json_response['shipping'])

    @property
    def card_personalization(self):
        if 'card_personalization' in self.json_response:
            return CardPersonalization(self.json_response['card_personalization'])

    @property
    def payment_instrument(self):
        if 'payment_instrument' in self.json_response:
            return self.json_response['payment_instrument']

    @property
    def package_id(self):
        if 'package_id' in self.json_response:
            return self.json_response['package_id']

    @property
    def all_zero_card_security_code(self):
        if 'all_zero_card_security_code' in self.json_response:
            return self.json_response['all_zero_card_security_code']

    @property
    def bin_prefix(self):
        if 'bin_prefix' in self.json_response:
            return self.json_response['bin_prefix']

    @property
    def bulk_ship(self):
        if 'bulk_ship' in self.json_response:
            return self.json_response['bulk_ship']

    @property
    def pan_length(self):
        if 'pan_length' in self.json_response:
            return self.json_response['pan_length']

    @property
    def fulfillment_provider(self):
        if 'fulfillment_provider' in self.json_response:
            return self.json_response['fulfillment_provider']

    @property
    def allow_card_creation(self):
        if 'allow_card_creation' in self.json_response:
            return self.json_response['allow_card_creation']

    @property
    def uppercase_name_lines(self):
        if 'uppercase_name_lines' in self.json_response:
            return self.json_response['uppercase_name_lines']

    @property
    def enable_offline_pin(self):
        if 'enable_offline_pin' in self.json_response:
            return self.json_response['enable_offline_pin']

    def __repr__(self):
         return '<Marqeta.response_models.card_product_fulfillment_response.CardProductFulfillmentResponse>'