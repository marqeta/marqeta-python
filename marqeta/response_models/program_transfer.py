from datetime import datetime, date
from marqeta.response_models.fee_model import FeeModel
from marqeta.response_models import datetime_object
import json
import re

class ProgramTransfer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def fees(self):
        if 'fees' in self.json_response:
            return [FeeModel(val) for val in self.json_response['fees']]

    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def user_token(self):
        return self.json_response.get('user_token', None)


    @property
    def business_token(self):
        return self.json_response.get('business_token', None)


    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def type_token(self):
        return self.json_response.get('type_token', None)


    @property
    def tags(self):
        return self.json_response.get('tags', None)


    @property
    def memo(self):
        return self.json_response.get('memo', None)


    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)


    def __repr__(self):
         return '<Marqeta.response_models.program_transfer.ProgramTransfer>' + self.__str__()
