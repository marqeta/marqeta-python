from datetime import datetime

class DigitalWalletTokenAddressVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def validate(self):
        if 'validate' in self.json_response:
            return self.json_response['validate']

