#!/usr/bin/env python3

'''MERCHANTS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.merchant_response_model import MerchantResponseModel
from marqeta.response_models.store_response_model import StoreResponseModel


class MerchantsCollection(object):
    '''
    Marqeta API 'merchants' endpoint list, create, find and update operations
    '''
    _endpoint = 'merchants'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, MerchantResponseModel)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: merchants token
        :return: MerchantContext object
        '''
        return MerchantContext(token, self.client)

    def page(self, count=5, start_index=0):
        '''
        Provides the requested page for merchants
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with MerchantResponseModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: MerchantResponseModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the merchants
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of MerchantResponseModel object
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an merchants object
        :param data: data required for creation
        :param params: query parameters
        :return: MerchantResponseModel object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific merchants object
        :param token: merchants token
        :param params: query parameters
        :return: MerchantResponseModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an merchants object
        :param token: merchants token
        :param data: data to be updated
        :return: MerchantResponseModel object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.merchants.MerchantsCollection>'


class MerchantContext(MerchantsCollection):
    ''' class to specify sub endpoints for merchants '''

    def __init__(self, token, client):
        super(MerchantContext, self).__init__(client)
        self.token = token
        self.stores = self.Stores(self.token, Collection(client, StoreResponseModel))

    class Stores(object):
        '''
        Lists the stores for merchant
        Returns StoreResponseModel object
        '''
        _endpoint = 'merchants/{}/stores'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0):
            return self.collection.page(endpoint=self._endpoint.format(self.token),
                                        count=count, start_index=start_index)

        def stream(self, params=None):
            return self.collection.stream(endpoint=self._endpoint.format(self.token),
                                          query_params=params)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint.format(self.token),
                                        query_params=params, limit=limit)

        def __repr__(self):
            return '<<Marqeta.resources.merchants.MerchantContext.Stores>'

    def __repr__(self):
        return '<<Marqeta.resources.merchants.MerchantContext>'
