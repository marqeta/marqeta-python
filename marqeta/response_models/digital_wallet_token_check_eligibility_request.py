from datetime import datetime, date
from marqeta.response_models.digital_wallet_token_card_info import DigitalWalletTokenCardInfo
import json

class DigitalWalletTokenCheckEligibilityRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'pan_source' : self.pan_source,
           'digital_wallet_token_card_data' : self.digital_wallet_token_card_data,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pan_source(self):
        if 'pan_source' in self.json_response:
            return self.json_response['pan_source']

    @property
    def digital_wallet_token_card_data(self):
        if 'digital_wallet_token_card_data' in self.json_response:
            return DigitalWalletTokenCardInfo(self.json_response['digital_wallet_token_card_data'])

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_check_eligibility_request.DigitalWalletTokenCheckEligibilityRequest>'