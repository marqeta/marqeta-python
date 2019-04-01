#!/usr/bin/env python3

"""GPA Order RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.gpa_response import GpaResponse
from marqeta.response_models.gpa_returns import GpaReturns


class GpaOrderCollection(object):
    '''
    Marqeta API 'gpaorders' endpoint list, create, find and update operations
    '''
    _endpoint = 'gpaorders'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, GpaResponse)
        self.unloads = Unloads(Collection(self.client, GpaReturns))

    def create(self, data={}):
        '''
        Creates an gpaorders object
        :param data: data required for creation
        :param params: query parameters
        :return: GpaResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific gpaorders object
        :param token: gpaorders token
        :param params: query parameters
        :return: GpaResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.gpa_order.GpaCollection>'


class Unloads(object):
    '''
    Lists, Creates and Finds the gpa order unloads
    Returns GpaReturns object
    '''
    _endpoint = 'gpaorders/unloads'

    def __init__(self, collection):
        self.collections = collection

    def page(self, count=5, start_index=0):
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.gpa_order.Unloads>'
