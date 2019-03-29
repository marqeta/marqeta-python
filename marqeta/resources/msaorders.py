#!/usr/bin/env python3

'''MSAORDERS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.msa_order_response import MsaOrderResponse
from marqeta.response_models.msa_returns import MsaReturns


class MsaOrdersCollection(object):
    _endpoint = 'msaorders'

    def __init__(self, client):
        '''
         Creates a client collection objects
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, MsaOrderResponse)
        self.unloads = MsaordersUnloadsCollection(Collection(self.client, MsaReturns))

    def create(self, data, params=None):
        '''
        Creates an msaorders object
        :param data: data required for creation
        :param params: query parameters
        :return: MsaOrderResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific msaorders object
        :param token: msaorders token
        :param params: query parameters
        :return: MsaOrderResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an msaorders object
        :param token: msaorders token
        :param data: data to be updated
        :return: MsaOrderResponse object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.msaorders.MsaOrdersCollection>'


class MsaordersUnloadsCollection(object):
    ''' Class for msaorder unloads '''
    _endpoint = 'msaorders/unloads'

    def __init__(self, collection):
        '''
        Lists, Creates and Finds the MsaOrder
        Returns MsaReturns object
        '''
        self.collections = collection

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.msaorders_unloads.MsaordersUnloadsCollection>'
