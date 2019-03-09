from datetime import datetime

class ActivationActions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def terminate_reissued_source_card(self):
        if 'terminate_reissued_source_card' in self.json_response:
            return self.json_response['terminate_reissued_source_card']

    @property
    def swap_digital_wallet_tokens_from_card_token(self):
        if 'swap_digital_wallet_tokens_from_card_token' in self.json_response:
            return self.json_response['swap_digital_wallet_tokens_from_card_token']

