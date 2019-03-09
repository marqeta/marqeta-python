from datetime import datetime
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.address_verification_source import AddressVerificationSource
from marqeta.response_models.address_verification_source import AddressVerificationSource

class JitAddressVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def request(self):
        if 'request' in self.json_response:
            return AvsInformation(self.json_response['request'])

    @property
    def issuer(self):
        if 'issuer' in self.json_response:
            return AddressVerificationSource(self.json_response['issuer'])

    @property
    def gateway(self):
        if 'gateway' in self.json_response:
            return AddressVerificationSource(self.json_response['gateway'])

