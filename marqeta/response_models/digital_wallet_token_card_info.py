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
        return self.json_response.get('pan', None)

    @property
    def exp_month(self):
        return self.json_response.get('exp_month', None)

    @property
    def exp_year(self):
        return self.json_response.get('exp_year', None)

    @property
    def cvv(self):
        return self.json_response.get('cvv', None)

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_token_card_info.DigitalWalletTokenCardInfo>' + self.__str__()
