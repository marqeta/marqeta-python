from datetime import datetime, date
from marqeta.response_models.fulfillment import Fulfillment
from marqeta.response_models.user_association import UserAssociation
from marqeta.response_models.expiration_offsét import ExpirationOffsét
import json

class BulkIssuanceRequest(object):

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
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return Fulfillment(self.json_response['fulfillment'])

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

    def __repr__(self):
         return '<Marqeta.response_models.bulk_issuance_request.BulkIssuanceRequest>'