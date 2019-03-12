#!/usr/bin/env python3
"""FUNDING SOURCES WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.cardholder_address_response import CardholderAddressResponse
from marqeta.response_models.funding_account_response_model import FundingAccountResponseModel
from marqeta.response_models.payment_card_response_model import PaymentCardResponseModel
from marqeta.response_models.program_funding_source_response import ProgramFundingSourceResponse
from marqeta.response_models.ach_response_model import AchResponseModel
from marqeta.response_models.ach_verification_model import AchVerificationModel


class FundingSourcesCollection(object):

    _endpoint = 'fundingsources'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CardholderAddressResponse)
        self.collections_business = Collection(self.client, FundingAccountResponseModel)
        self.ach = Ach(self.client, Collection(self.client, AchResponseModel))
        self.addresses = Addresses(Collection(self.client, CardholderAddressResponse))
        self.payment_card = PaymentCard(Collection(self.client, PaymentCardResponseModel))
        self.program_gateway = ProgramGateway(Collection(self.client, ProgramFundingSourceResponse))
        self.program = Program(Collection(self.client, ProgramFundingSourceResponse))
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    def stream_for_user(self, user_token, params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint+'/users/{}'.format(user_token), query_params=self.query_params)

    def stream_for_business(self, business_token, params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint+'/business/{}'.format(business_token), query_params=self.query_params)

    def list_for_user(self, user_token, params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=self._endpoint+'/users/{}'.format(user_token),
                                     query_params=self.query_params, limit=limit)

    def list_for_business(self, business_token, params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections_business.list(endpoint=self._endpoint+'/business/{}'.format(business_token),
                                              query_params=self.query_params, limit=limit)

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.FundingSourcesCollection>'


class AchContext(object):

    def __init__(self, token, collection):
        self.token = token
        self.collections = collection

    def verification_amounts(self, params=None):
        return self.collections.find(endpoint='fundingsources/ach/{}/verificationamounts'.format(self.token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.AchContext>'


class Addresses(object):

    _endpoint = 'fundingsources/addresses'

    def __init__(self, collection):
        self.collections = collection
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    def stream_for_user(self,user_token, params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint + '/user/{}'.format(user_token), query_params=self.query_params)

    def stream_for_business(self,business_token, params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint +'/business/{}'.format(business_token), query_params=self.query_params)

    def list_for_user(self, user_token, params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=self._endpoint + '/user/{}'.format(user_token),
                                     query_params=self.query_params, limit=limit)

    def list_for_business(self, business_token, params=None,
                          limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=self._endpoint +'/business/{}'.format(business_token),
                                     query_params=self.query_params, limit=limit)

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.Addresses>'


class Ach(object):

    _endpoint = 'fundingsources/ach'

    def __init__(self, client, collection):
        self.client = client
        self.collections = collection

    def __call__(self, token):
        return AchContext(token, Collection(self.client, AchVerificationModel))

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.Ach>'


class PaymentCard(object):

    _endpoint = 'fundingsources/paymentcard'

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.PaymentCard>'

class ProgramGateway(object):

    _endpoint = 'fundingsources/programgateway'

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.ProgramGateway>'


class Program(object):

    _endpoint = 'fundingsources/program'

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, funding_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.funding_sources.Program>'
