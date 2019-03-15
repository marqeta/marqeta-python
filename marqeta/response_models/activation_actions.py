from datetime import datetime, date
import json

class ActivationActions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'terminate_reissued_source_card' : self.terminate_reissued_source_card,
           'swap_digital_wallet_tokens_from_card_token' : self.swap_digital_wallet_tokens_from_card_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def terminate_reissued_source_card(self):
        if 'terminate_reissued_source_card' in self.json_response:
            return self.json_response['terminate_reissued_source_card']

    @property
    def swap_digital_wallet_tokens_from_card_token(self):
        if 'swap_digital_wallet_tokens_from_card_token' in self.json_response:
            return self.json_response['swap_digital_wallet_tokens_from_card_token']

    def __repr__(self):
         return '<Marqeta.response_models.activation_actions.ActivationActions>'