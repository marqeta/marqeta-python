

'''FUNDINGSOURCES/USER/{USER_TOKEN} RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.funding_account_response_model import FundingAccountResponseModel

from marqeta.response_models.cardholder_address_response import CardholderAddressResponse
from marqeta.response_models.payment_card_response_model import PaymentCardResponseModel
from marqeta.response_models.program_funding_source_response import ProgramFundingSourceResponse
from marqeta.response_models.gateway_program_funding_source_response import GatewayProgramFundingSourceResponse
from marqeta.response_models.ach_response_model import AchResponseModel
from marqeta.response_models.ach_verification_model import AchVerificationModel

class FundingSourcesCollection(object):
    '''
    Marqeta API 'fundingsources/user/{user_token}' endpoint list, create, find and update operations
    '''

    _endpoint = 'fundingsources'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, FundingAccountResponseModel)

        self.ach = Ach(self.client, Collection(self.client, AchResponseModel))
        self.addresses = Addresses(Collection(self.client, CardholderAddressResponse))
        self.payment_card = PaymentCard(Collection(self.client, PaymentCardResponseModel))
        self.program_gateway = ProgramGateway(Collection(self.client,
                                                         GatewayProgramFundingSourceResponse))
        self.program = Program(Collection(self.client, ProgramFundingSourceResponse))

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: fundingsources token
        :return: FundingAccountResponseModel object
        '''
        return FundingSourceMakeDefualt(token, self.client)

    def page_for_user(self, user_token, count=5, start_index=0, params=None):
        '''
        Provides the requested page for kyc
        :param user_token: user token
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with KycResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + '/user/{}'.format(user_token),
                                     count=count, start_index=start_index, query_params=params)

    def page_for_business(self, business_token, count=5, start_index=0, params=None):
        '''
        Provides the requested page for kyc
        :param business_token: user token
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with KycResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + '/business/{}'.
                                     format(business_token), count=count, start_index=start_index,
                                     query_params=params)

    def stream_for_user(self, user_token, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param user_token: user token
        :param params: query parameters
        :return: KycResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint + '/user/{}'.format(user_token),
                                       query_params=params)

    def stream_for_business(self, business_token, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param business_token: user token
        :param params: query parameters
        :return: KycResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint + '/business/{}'.
                                       format(business_token), query_params=params)

    def list_for_user(self, user_token, params=None, limit=None):
        '''
        List all the kyc for user
        :param params: query parameters
        :param limit: parameter to limit the list count
        :param user_token: user token
        :param params:
        :return: List of KycResponse object:
        '''
        return self.collections.list(endpoint=self._endpoint + '/user/{}'.format(user_token),
                                     query_params=params, limit=limit)

    def list_for_business(self, business_token, params=None, limit=None):
        '''
        List kyc for business
        :param params: query parameters
        :param limit: parameter to limit the list count
        :param business_token: business token
        :param params:
        :return: List of KycResponse object:
        '''
        return self.collections.list(endpoint=self._endpoint + '/business/{}'.
                                     format(business_token), query_params=params, limit=limit)
    def __repr__(self):
        return '<Marqeta.resources.funding_sources.FundingSourcesCollection>'

class FundingSourceMakeDefualt(FundingSourcesCollection):
    '''
    Class to make a default funding source
    Returns PaymentCardResponseModel object
    '''

    def __init__(self, token, client):
        super(FundingSourceMakeDefualt, self).__init__(client)
        self.token = token
        self.collections = Collection(self.client, PaymentCardResponseModel)

    def make_default(self):
        return self.collections.save(data={}, endpoint='fundingsources/{}/default'.
                                     format(self.token))


class AchContext(object):
    '''
    class for account verification model
    Returns AchVerificationModel object
    '''

    def __init__(self, token, collection):
        self.token = token
        self.collections = collection

    def verification_amounts(self, params=None):
        return self.collections.find(endpoint='fundingsources/ach/{}/verificationamounts'.
                                     format(self.token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.AchContext>'


class Addresses(object):
    '''
    Lists, Creates, UPdates and Finds the funding address
    Returns CardholderAddressResponse object
    '''
    _endpoint = 'fundingsources/addresses'

    def __init__(self, collection):
        self.collections = collection

    def page_for_user(self, user_token, count=5, start_index=0, params=None):
        return self.collections.page(endpoint=self._endpoint + '/user/{}'.
                                     format(user_token), count=count,
                                     start_index=start_index, query_params=params)

    def page_for_business(self, business_token, count=5, start_index=0, params=None):
        return self.collections.page(endpoint=self._endpoint + '/business/{}'.
                                     format(business_token), count=count,
                                     start_index=start_index, query_params=params)

    def stream_for_user(self, user_token, params=None):
        return self.collections.stream(endpoint=self._endpoint + '/user/{}'.
                                       format(user_token), query_params=params)

    def stream_for_business(self, business_token, params=None):
        return self.collections.stream(endpoint=self._endpoint + '/business/{}'.
                                       format(business_token), query_params=params)

    def list_for_user(self, user_token, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint + '/user/{}'.
                                     format(user_token), query_params=params, limit=limit)

    def list_for_business(self, business_token, params=None,
                          limit=None):
        return self.collections.list(endpoint=self._endpoint + '/business/{}'.
                                     format(business_token),
                                     query_params=params, limit=limit)

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.Addresses>'


class Ach(object):
    '''
    Lists, Creates, Updates and Finds the funding address
    Returns AchResponseModel object
    '''
    _endpoint = 'fundingsources/ach'

    def __init__(self, client, collection):
        self.client = client
        self.collections = collection

    def __call__(self, token):
        return AchContext(token, Collection(self.client, AchVerificationModel))

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token),
                                     query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.Ach>'


class PaymentCard(object):
    '''
    Creates, Updates and Finds the funding address
    Returns PaymentCardResponseModel object
    '''
    _endpoint = 'fundingsources/paymentcard'

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token),
                                     query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.PaymentCard>'


class ProgramGateway(object):
    '''
    Creates, Updates and Finds the funding address
    Returns GatewayProgramFundingSourceResponse object
    '''
    _endpoint = 'fundingsources/programgateway'

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token),
                                     query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.ProgramGateway>'


class Program(object):
    '''
    Creates, Updates and Finds the funding address
    Returns ProgramFundingSourceResponse object
    '''
    _endpoint = 'fundingsources/program'

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token),
                                     query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.Program>'
