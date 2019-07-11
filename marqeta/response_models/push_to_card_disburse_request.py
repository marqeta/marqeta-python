from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class PushToCardDisburseRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def tags(self):
        return self.json_response.get('tags', None)


    @property
    def memo(self):
        return self.json_response.get('memo', None)


    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)


    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def payment_instrument_token(self):
        return self.json_response.get('payment_instrument_token', None)


    def __repr__(self):
         return '<Marqeta.response_models.push_to_card_disburse_request.PushToCardDisburseRequest>' + self.__str__()
