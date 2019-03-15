from datetime import datetime, date
from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.address_verification_source import AddressVerificationSource
from marqeta.response_models.address_verification_source import AddressVerificationSource
import json

class JitAddressVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'request' : self.request,
           'issuer' : self.issuer,
           'gateway' : self.gateway,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.jit_address_verification.JitAddressVerification>'