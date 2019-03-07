from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.address_verification_source import AddressVerificationSource


class GatewayLogModel(object):

    def __init__(self, response):
        self.response = response

    @property
    def order_number(self):
        if 'order_number' in self.response:
            return self.response['order_number']

    @property
    def transaction_id(self):
        if 'transaction_id' in self.response:
            return self.response['transaction_id']

    @property
    def message(self):
        if 'message' in self.response:
            return self.response['message']

    @property
    def duration(self):
        if 'duration' in self.response:
            return self.response['duration']

    @property
    def timed_out(self):
        if 'timed_out' in self.response:
            return self.response['timed_out']

    @property
    def response(self):
        if 'response' in self.response:
            return GatewayResponse(self.response['response'])


class GatewayResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def code(self):
        if 'code' in self.response:
            return self.response['code']

    @property
    def data(self):
        if 'data' in self.response:
            return JitProgramResponse(self.response['data'])


class JitProgramResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def jit_funding(self):
        if 'jit_funding' in self.response:
            return JitFundingApi(self.response['jit_funding'])


class JitFundingApi(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def method(self):
        if 'method' in self.response:
            return self.response['method']

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def acting_user_token(self):
        if 'acting_user_token' in self.response:
            return self.response['acting_user_token']

    @property
    def business_token(self):
        if 'business_token' in self.response:
            return self.response['business_token']

    @property
    def amount(self):
        if 'amount' in self.response:
            return self.response['amount']

    @property
    def memo(self):
        if 'memo' in self.response:
            return self.response['memo']

    @property
    def tags(self):
        if 'tags' in self.response:
            return self.response['tags']

    @property
    def original_jit_funding_token(self):
        if 'original_jit_funding_token' in self.response:
            return self.response['original_jit_funding_token']

    @property
    def incremental_authorization_jit_funding_tokens(self):
        if 'incremental_authorization_jit_funding_tokens' in self.response:
            return self.response['incremental_authorization_jit_funding_tokens']

    @property
    def address_verification(self):
        if 'address_verification' in self.response:
            return JitAddressVerification(self.response['address_verification'])


class JitAddressVerification(object):

    def __init__(self, response):
        self.response = response

    @property
    def request(self):
        if 'request' in self.response:
            return AvsInformation(self.response['request'])

    @property
    def issuer(self):
        if 'issuer' in self.response:
            return AddressVerificationSource(self.response['issuer'])

    @property
    def gateway(self):
        if 'gateway' in self.response:
            return AddressVerificationSource(self.response['gateway'])
