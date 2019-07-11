from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class PaymentCardResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime_object('created_time', self.json_response)


    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime_object('last_modified_time', self.json_response)


    @property
    def type(self):
        return self.json_response.get('type', None)


    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def account_suffix(self):
        return self.json_response.get('account_suffix', None)


    @property
    def account_type(self):
        return self.json_response.get('account_type', None)


    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def is_default_account(self):
        return self.json_response.get('is_default_account', None)

    @property
    def exp_date(self):
        return self.json_response.get('exp_date', None)


    @property
    def user_token(self):
        return self.json_response.get('user_token', None)


    @property
    def business_token(self):
        return self.json_response.get('business_token', None)


    def __repr__(self):
         return '<Marqeta.response_models.payment_card_response_model.PaymentCardResponseModel>' + self.__str__()
