"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime

class ActivationActions(object):

    def __init__(self, response):
        self.response = response

    @property
    def terminate_reissued_source_card(self):
        if 'terminate_reissued_source_card' in self.response:
            return self.response['terminate_reissued_source_card']

    @property
    def swap_digital_wallet_tokens_from_card_token(self):
        if 'swap_digital_wallet_tokens_from_card_token' in self.response:
            return self.response['swap_digital_wallet_tokens_from_card_token']
