from datetime import datetime, date
from marqeta.response_models.card_fulfillment_response import CardFulfillmentResponse
from marqeta.response_models.user_association import UserAssociation
from marqeta.response_models.expiration_offsét import ExpirationOffsét
import json

class BulkIssuanceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'fulfillment' : self.fulfillment,
           'expedite' : self.expedite,
           'card_product_token' : self.card_product_token,
           'card_allocation' : self.card_allocation,
           'user_association' : self.user_association,
           'name_line_1_numeric_postfix' : self.name_line_1_numeric_postfix,
           'expiration_offset' : self.expiration_offset,
           'cards_processed' : self.cards_processed,
           'created_time' : self.created_time,
           'name_line1_start_index' : self.name_line1_start_index,
           'name_line1_end_index' : self.name_line1_end_index,
           'card_fulfillment_time' : self.card_fulfillment_time,
           'provider_ship_date' : self.provider_ship_date,
           'provider_shipping_method' : self.provider_shipping_method,
           'provider_tracking_number' : self.provider_tracking_number,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return CardFulfillmentResponse(self.json_response['fulfillment'])

    @property
    def expedite(self):
        if 'expedite' in self.json_response:
            return self.json_response['expedite']

    @property
    def card_product_token(self):
        if 'card_product_token' in self.json_response:
            return self.json_response['card_product_token']

    @property
    def card_allocation(self):
        if 'card_allocation' in self.json_response:
            return self.json_response['card_allocation']

    @property
    def user_association(self):
        if 'user_association' in self.json_response:
            return UserAssociation(self.json_response['user_association'])

    @property
    def name_line_1_numeric_postfix(self):
        if 'name_line_1_numeric_postfix' in self.json_response:
            return self.json_response['name_line_1_numeric_postfix']

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffsét(self.json_response['expiration_offset'])

    @property
    def cards_processed(self):
        if 'cards_processed' in self.json_response:
            return self.json_response['cards_processed']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def name_line1_start_index(self):
        if 'name_line1_start_index' in self.json_response:
            return self.json_response['name_line1_start_index']

    @property
    def name_line1_end_index(self):
        if 'name_line1_end_index' in self.json_response:
            return self.json_response['name_line1_end_index']

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
        if 'provider_shipping_method' in self.json_response:
            return self.json_response['provider_shipping_method']

    @property
    def provider_tracking_number(self):
        if 'provider_tracking_number' in self.json_response:
            return self.json_response['provider_tracking_number']

    def __repr__(self):
         return '<Marqeta.response_models.bulk_issuance_response.BulkIssuanceResponse>'