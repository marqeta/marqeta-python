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

    def stream_for_user(self, endpoint='fundingsources/users', params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    def stream_for_business(self, endpoint='fundingsources/business', params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    def list_for_user(self, user_token, endpoint='fundingsources/user', params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=endpoint + '/{}'.format(user_token),
                                     query_params=self.query_params, limit=limit)

    def list_for_business(self, business_token, endpoint='fundingsources/business', params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections_business.list(endpoint=endpoint + '/{}'.format(business_token),
                                              query_params=self.query_params, limit=limit)


class AchContext(object):

    def __init__(self, token, collection):
        self.token = token
        self.collections = collection

    def verification_amounts(self, endpoint='fundingsources/ach', params=None):
        return self.collections.find(endpoint=endpoint + '/{}/verificationamounts'.format(self.token),
                                     query_params=params)


class Addresses(object):

    def __init__(self, collection):
        self.collections = collection
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    def stream_for_user(self, endpoint='fundingsources/addresses/user', params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    def stream(self, endpoint='fundingsources/addresses/business', params=None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    def list_for_user(self, user_token, endpoint='fundingsources/addresses/user', params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=endpoint + '/{}'.format(user_token),
                                     query_params=self.query_params, limit=limit)

    def list_for_business(self, business_token, endpoint='fundingsources/addresses/business', params=None,
                          limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=endpoint + '/{}'.format(business_token),
                                     query_params=self.query_params, limit=limit)

    def create(self, data={}, endpoint='users'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, token, endpoint='fundingsources/addresses', params=None):
        return self.collections.find(endpoint=endpoint + '/{}'.format(token), query_params=params)

    def save(self, token, data, endpoint='fundingsources/addresses'):
        return self.collections.save(data, endpoint=endpoint + '/{}'.format(token))


class Ach(object):

    def __init__(self, client, collection):
        self.client = client
        self.collections = collection

    def __call__(self, token):
        return AchContext(token, Collection(self.client, AchVerificationModel))

    def create(self, data={}, endpoint='fundingsources/ach'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, funding_token, endpoint='fundingsources/ach', params=None):
        return self.collections.find(endpoint=endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data, endpoint='fundingsources/ach'):
        return self.collections.save(data, endpoint=endpoint + '/{}'.format(token))


class PaymentCard(object):

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}, endpoint='fundingsources/paymentcard'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, funding_token, endpoint='fundingsources/paymentcard', params=None):
        return self.collections.find(endpoint=endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data, endpoint='fundingsources/paymentcard'):
        return self.collections.save(data, endpoint=endpoint + '/{}'.format(token))


class ProgramGateway(object):

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}, endpoint='fundingsources/programgateway'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, funding_token, endpoint='fundingsources/programgateway', params=None):
        return self.collections.find(endpoint=endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data, endpoint='fundingsources/programgateway'):
        return self.collections.save(data, endpoint=endpoint + '/{}'.format(token))


class Program(object):

    def __init__(self, collection):
        self.collections = collection

    def create(self, data={}, endpoint='fundingsources/program'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, funding_token, endpoint='fundingsources/program', params=None):
        return self.collections.find(endpoint=endpoint + '/{}'.format(funding_token), query_params=params)

    def save(self, token, data, endpoint='fundingsources/program'):
        return self.collections.save(data, endpoint=endpoint + '/{}'.format(token))
