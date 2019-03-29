from datetime import datetime, date
from marqeta.response_models.funding_source_model import FundingSourceModel
import json


class ProgramGatewayFundingSourceModel(FundingSourceModel):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    def __repr__(self):
        return '<Marqeta.response_models.program_gateway_funding_source_model.ProgramGatewayFundingSourceModel>'
