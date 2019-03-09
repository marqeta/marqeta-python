from datetime import datetime
from marqeta.response_models.digital_wallet_token_address_verification import DigitalWalletTokenAddressVerification

class WalletProviderCardOnFile(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def enabled(self):
        if 'enabled' in self.json_response:
            return self.json_response['enabled']

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return DigitalWalletTokenAddressVerification(self.json_response['address_verification'])

