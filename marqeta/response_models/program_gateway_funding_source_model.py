from datetime import datetime
from marqeta.response_models.funding_source_model import FundingSourceModel

class ProgramGatewayFundingSourceModel(FundingSourceModel):

    def __init__(self, json_response):
        self.json_response = json_response

