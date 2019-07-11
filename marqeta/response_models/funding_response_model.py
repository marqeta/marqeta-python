from datetime import datetime, date
from marqeta.response_models.gatewaylog import Gatewaylog
from marqeta.response_models import datetime_object
import json
import re

class FundingResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def id(self):
        return self.json_response.get('id', None)

    @property
    def accounting_balance(self):
        return self.json_response.get('accounting_balance', None)

    @property
    def available_balance(self):
        return self.json_response.get('available_balance', None)

    @property
    def transaction(self):
        if 'transaction' in self.json_response:
            return Gatewaylog(self.json_response['transaction'])

    def __repr__(self):
         return '<Marqeta.response_models.funding_response_model.FundingResponseModel>' + self.__str__()
