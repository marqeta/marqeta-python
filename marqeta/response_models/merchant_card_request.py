from datetime import datetime, date
from marqeta.response_models.expiration_offsét import ExpirationOffsét
import json


class MerchantCardRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_product_token(self):
        return self.json_response.get('card_product_token', None)

    @property
    def expedite(self):
        return self.json_response.get('expedite', None)

    @property
    def metadata(self):
        return self.json_response.get('metadata', None)

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffsét(self.json_response['expiration_offset'])

    def __repr__(self):
        return '<Marqeta.response_models.merchant_card_request.MerchantCardRequest>' + self.__str__()
