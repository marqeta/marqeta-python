from datetime import datetime, date
import json

class DigitalWalletTokenCardInfo(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pan(self):
        if 'pan' in self.json_response:
            return self.json_response['pan']

    @property
    def exp_month(self):
        if 'exp_month' in self.json_response:
            return self.json_response['exp_month']

    @property
    def exp_year(self):
        if 'exp_year' in self.json_response:
            return self.json_response['exp_year']

    @property
    def cvv(self):
        if 'cvv' in self.json_response:
            return self.json_response['cvv']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_card_info.DigitalWalletTokenCardInfo>'