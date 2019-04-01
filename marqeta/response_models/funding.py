from datetime import datetime, date
from marqeta.response_models.funding_source_model import FundingSourceModel
from marqeta.response_models.cardholder_address_response import CardholderAddressResponse
from marqeta.response_models.gateway_log_model import GatewayLogModel
import json


class Funding(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def source(self):
        if 'source' in self.json_response:
            return FundingSourceModel(self.json_response['source'])

    @property
    def source_address(self):
        if 'source_address' in self.json_response:
            return CardholderAddressResponse(self.json_response['source_address'])

    @property
    def gateway_log(self):
        if 'gateway_log' in self.json_response:
            return GatewayLogModel(self.json_response['gateway_log'])

    def __repr__(self):
        return '<Marqeta.response_models.funding.Funding>' + self.__str__()
