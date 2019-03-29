from datetime import datetime, date
from marqeta.response_models.token_service_provider import TokenServiceProvider
from marqeta.response_models.device import Device
from marqeta.response_models.wallet_provider_profile import WalletProviderProfile
from marqeta.response_models.address_verification import AddressVerification
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse
import json


class DigitalWalletToken(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):

        return self.json_response.get('token', None)

    @property
    def card_token(self):

        return self.json_response.get('card_token', None)

    @property
    def state(self):

        return self.json_response.get('state', None)

    @property
    def state_reason(self):

        return self.json_response.get('state_reason', None)

    @property
    def fulfillment_status(self):

        return self.json_response.get('fulfillment_status', None)

    @property
    def issuer_eligibility_decision(self):

        return self.json_response.get('issuer_eligibility_decision', None)

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

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_token.DigitalWalletToken>'
