from datetime import datetime, date
from marqeta.response_models.push_tokenize_request_data import PushTokenizeRequestData
import json

class DigitalWalletAndroidPayProvisionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'card_token' : self.card_token,
           'push_tokenize_request_data' : self.push_tokenize_request_data,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def push_tokenize_request_data(self):
        if 'push_tokenize_request_data' in self.json_response:
            return PushTokenizeRequestData(self.json_response['push_tokenize_request_data'])

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_android_pay_provision_response.DigitalWalletAndroidPayProvisionResponse>'