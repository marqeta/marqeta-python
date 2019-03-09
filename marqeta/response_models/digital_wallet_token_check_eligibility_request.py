from datetime import datetime
from marqeta.response_models.digital_wallet_token_card_info import DigitalWalletTokenCardInfo

class DigitalWalletTokenCheckEligibilityRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def pan_source(self):
        if 'pan_source' in self.json_response:
            return self.json_response['pan_source']

    @property
    def digital_wallet_token_card_data(self):
        if 'digital_wallet_token_card_data' in self.json_response:
            return DigitalWalletTokenCardInfo(self.json_response['digital_wallet_token_card_data'])

