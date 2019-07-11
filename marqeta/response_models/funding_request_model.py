from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class FundingRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)


    @property
    def order_number(self):
        return self.json_response.get('order_number', None)


    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def funding_source(self):
        return self.json_response.get('funding_source', None)


    @property
    def funding_address(self):
        return self.json_response.get('funding_address', None)


    @property
    def fundgpadetail(self):
        return self.json_response.get('fundgpadetail', None)


    @property
    def order_token(self):
        return self.json_response.get('order_token', None)


    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)


    def __repr__(self):
         return '<Marqeta.response_models.funding_request_model.FundingRequestModel>' + self.__str__()
