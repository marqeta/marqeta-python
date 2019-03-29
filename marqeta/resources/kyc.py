#!/usr/bin/env python3

'''KYC RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.kyc_response import KycResponse


class KycCollection(object):
    '''
    Marqeta API 'kyc' endpoint list, create, find and update operations
    '''
    _endpoint = 'kyc'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, KycResponse)

    def page_for_user(self, user_token, params=None):
        '''
        Provides the requested page for kyc
        :param user_token: user token
        :param params: query parameters
        :return: requested page with KycResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + '/user/{}'.format(user_token),
                                     query_params=params)

    def page_for_business(self, business_token, params=None):
        '''
        Provides the requested page for kyc
        :param business_token: user token
        :param params: query parameters
        :return: requested page with KycResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + '/business/{}'.
                                     format(business_token), query_params=params)

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
        :param user_token: user token
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

    def create(self, data={}):
        '''
        Creates an kyc object
        :param data: data required for creation
        :param params: query parameters
        :return: KycResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific kyc object
        :param token: kyc token
        :param params: query parameters
        :return: KycResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an kyc object
        :param token: kyc token
        :param data: data to be updated
        :return: KycResponse object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.kyc.KycCollection>'
