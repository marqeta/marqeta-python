from datetime import datetime, date
from marqeta.response_models.shipping import Shipping
from marqeta.response_models.card_personalization import CardPersonalization
import json


class CardProductFulfillment(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def shipping(self):

        if 'shipping' in self.json_response:
            return Shipping(self.json_response['shipping'])

    @property
    def card_personalization(self):

        if 'card_personalization' in self.json_response:
            return CardPersonalization(self.json_response['card_personalization'])

    @property
    def payment_instrument(self):

        return self.json_response.get('payment_instrument', None)

    @property
    def package_id(self):

        return self.json_response.get('package_id', None)

    @property
    def all_zero_card_security_code(self):

        return self.json_response.get('all_zero_card_security_code', None)

    @property
    def bin_prefix(self):

        return self.json_response.get('bin_prefix', None)

    @property
    def bulk_ship(self):

        return self.json_response.get('bulk_ship', None)

    @property
    def pan_length(self):

        return self.json_response.get('pan_length', None)

    @property
    def fulfillment_provider(self):

        return self.json_response.get('fulfillment_provider', None)

    @property
    def allow_card_creation(self):

        return self.json_response.get('allow_card_creation', None)

    @property
    def uppercase_name_lines(self):

        return self.json_response.get('uppercase_name_lines', None)

    @property
    def enable_offline_pin(self):

        return self.json_response.get('enable_offline_pin', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_product_fulfillment.CardProductFulfillment>'
