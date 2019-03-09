from datetime import datetime
from marqeta.response_models.token_service_provider import TokenServiceProvider
from marqeta.response_models.device import Device
from marqeta.response_models.wallet_provider_profile import WalletProviderProfile
from marqeta.response_models.address_verification import AddressVerification
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse

class DigitalWalletToken(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def state_reason(self):
        if 'state_reason' in self.json_response:
            return self.json_response['state_reason']

    @property
    def fulfillment_status(self):
        if 'fulfillment_status' in self.json_response:
            return self.json_response['fulfillment_status']

    @property
    def issuer_eligibility_decision(self):
        if 'issuer_eligibility_decision' in self.json_response:
            return self.json_response['issuer_eligibility_decision']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token_service_provider(self):
        if 'token_service_provider' in self.json_response:
            return TokenServiceProvider(self.json_response['token_service_provider'])

    @property
    def device(self):
        if 'device' in self.json_response:
            return Device(self.json_response['device'])

    @property
    def wallet_provider_profile(self):
        if 'wallet_provider_profile' in self.json_response:
            return WalletProviderProfile(self.json_response['wallet_provider_profile'])

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return AddressVerification(self.json_response['address_verification'])

    @property
    def user(self):
        if 'user' in self.json_response:
            return UserCardHolderResponse(self.json_response['user'])

