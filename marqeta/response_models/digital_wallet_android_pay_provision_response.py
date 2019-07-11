from datetime import datetime, date
from marqeta.response_models.push_tokenize_request_data import PushTokenizeRequestData
from marqeta.response_models import datetime_object
import json
import re

class DigitalWalletAndroidPayProvisionResponse(object):

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
    def card_token(self):
        return self.json_response.get('card_token', None)


    @property
    def push_tokenize_request_data(self):
        if 'push_tokenize_request_data' in self.json_response:
            return PushTokenizeRequestData(self.json_response['push_tokenize_request_data'])

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_android_pay_provision_response.DigitalWalletAndroidPayProvisionResponse>' + self.__str__()
