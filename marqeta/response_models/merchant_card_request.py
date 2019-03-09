from datetime import datetime
from marqeta.response_models.expiration_offsét import ExpirationOffsét

class MerchantCardRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def card_product_token(self):
        if 'card_product_token' in self.json_response:
            return self.json_response['card_product_token']

    @property
    def expedite(self):
        if 'expedite' in self.json_response:
            return self.json_response['expedite']

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffsét(self.json_response['expiration_offset'])

