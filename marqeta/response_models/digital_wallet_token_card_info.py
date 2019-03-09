from datetime import datetime

class DigitalWalletTokenCardInfo(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

