from datetime import datetime, date
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.user_association import UserAssociation
from marqeta.response_models.expiration_offsét import ExpirationOffsét
import json


class BulkIssuanceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):

        return self.json_response.get('token', None)

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return CardFulfillmentResponse(self.json_response['fulfillment'])

    @property
    def expedite(self):
        return self.json_response.get('expedite', None)

    @property
    def card_product_token(self):
        return self.json_response.get('card_product_token', None)

    @property
    def card_allocation(self):
        return self.json_response.get('card_allocation', None)

    @property
    def user_association(self):
        if 'user_association' in self.json_response:
            return UserAssociation(self.json_response['user_association'])

    @property
    def name_line_1_numeric_postfix(self):
        return self.json_response.get('name_line_1_numeric_postfix', None)

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffsét(self.json_response['expiration_offset'])

    @property
    def cards_processed(self):
        return self.json_response.get('cards_processed', None)

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def name_line1_start_index(self):
        return self.json_response.get('name_line1_start_index', None)

    @property
    def name_line1_end_index(self):
       return self.json_response.get('name_line1_end_index', None)

    @property
    def card_fulfillment_time(self):
        if 'card_fulfillment_time' in self.json_response:
            return datetime.strptime(self.json_response['card_fulfillment_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def provider_ship_date(self):
        if 'provider_ship_date' in self.json_response:
            return datetime.strptime(self.json_response['provider_ship_date'], '%Y-%m-%d').date()

    @property
    def provider_shipping_method(self):
        return self.json_response.get('provider_shipping_method', None)

    @property
    def provider_tracking_number(self):
        return self.json_response.get('provider_tracking_number', None)

    def __repr__(self):
        return '<Marqeta.response_models.bulk_issuance_response.BulkIssuanceResponse>'
