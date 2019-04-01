from datetime import datetime, date
import json


class ActivationActions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def terminate_reissued_source_card(self):
        return self.json_response.get('terminate_reissued_source_card', None)

    @property
    def swap_digital_wallet_tokens_from_card_token(self):
        return self.json_response.get('swap_digital_wallet_tokens_from_card_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.activation_actions.ActivationActions>' + self.__str__()
