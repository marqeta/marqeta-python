from datetime import datetime, date
from marqeta.response_models.fee import Fee
from marqeta.response_models import datetime_object
import json
import re

class FeeDetail(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def memo(self):
        return self.json_response.get('memo', None)


    @property
    def tags(self):
        return self.json_response.get('tags', None)


    @property
    def transaction_token(self):
        return self.json_response.get('transaction_token', None)


    @property
    def fee(self):
        if 'fee' in self.json_response:
            return Fee(self.json_response['fee'])

    def __repr__(self):
         return '<Marqeta.response_models.fee_detail.FeeDetail>' + self.__str__()
