from datetime import datetime
from marqeta.response_models.funding_source_model import FundingSourceModel

class ChargebackFundingSourceModel(FundingSourceModel):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def credit(self):
        if 'credit' in self.json_response:
            return self.json_response['credit']

