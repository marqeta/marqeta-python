from marqeta.response_models.funding_source_model import FundingSourceModel
from marqeta.response_models.cardholder_address_response import CardholderAddressResponse

class Funding(object):

    def __init__(self, response):
        self.response = response

    @property
    def amount(self):
        if 'amount' in self.response:
          return self.response['amount']
        
        
    @property
    def source(self):
        if 'source' in self.response:
        
            return FundingSourceModel(self.response['source'])
        
    @property
    def source_address(self):
        if 'source_address' in self.response:
        
            return CardholderAddressResponse(self.response['source_address'])
        
    @property
    def gateway_log(self):
        if 'gateway_log' in self.response:
        
            return gateway_log(self.response['gateway_log'])
        


