from marqeta.response_models.avs_information import AvsInformation
from marqeta.response_models.address_verification_source import AddressVerificationSource


class GatewayLogModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def order_number(self):
        if 'order_number' in self.json_response:
            return self.json_response['order_number']

    @property
    def transaction_id(self):
        if 'transaction_id' in self.json_response:
            return self.json_response['transaction_id']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

    @property
    def duration(self):
        if 'duration' in self.json_response:
            return self.json_response['duration']

    @property
    def timed_out(self):
        if 'timed_out' in self.json_response:
            return self.json_response['timed_out']

    @property
    def response(self):
        if 'response' in self.json_response:
            return GatewayResponse(self.json_response['response'])


class GatewayResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def code(self):
        if 'code' in self.json_response:
            return self.json_response['code']

    @property
    def data(self):
        if 'data' in self.json_response:
            return JitProgramResponse(self.json_response['data'])


class JitProgramResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def jit_funding(self):
        if 'jit_funding' in self.json_response:
            return JitFundingApi(self.json_response['jit_funding'])


class JitFundingApi(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def method(self):
        if 'method' in self.json_response:
            return self.json_response['method']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def acting_user_token(self):
        if 'acting_user_token' in self.json_response:
            return self.json_response['acting_user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def original_jit_funding_token(self):
        if 'original_jit_funding_token' in self.json_response:
            return self.json_response['original_jit_funding_token']

    @property
    def incremental_authorization_jit_funding_tokens(self):
        if 'incremental_authorization_jit_funding_tokens' in self.json_response:
            return self.json_response['incremental_authorization_jit_funding_tokens']

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return JitAddressVerification(self.json_response['address_verification'])


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
