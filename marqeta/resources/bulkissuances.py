#!/usr/bin/env python3

from marqeta.resources.collection import Collection
from marqeta.response_models.bulk_issuance_response import BulkIssuanceResponse


class BulkIssuancesCollection(object):
    '''
    Marqeta API 'bulkissuances' endpoint list, create, find and update operations
    '''
    _endpoint = 'bulkissuances'

    def __init__(self, client):
        '''
        Creates a client collection object
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, BulkIssuanceResponse)

    def page(self, count=5, start_index=0, params=None):
        '''
        Provides the requested page for bulkissuances
        :param count: data to be displayed per page
        :param start_index: start_index
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index,query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: BulkIssuanceResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the bulkissuances
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of BulkIssuanceResponse object
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an bulkissuances object
        :param data: data required for creation
        :param params: query parameters
        :return: BulkIssuanceResponse object of the created country
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Updates the existing country data
        :param token: bulkissuances token to update
        :param data: data to be updated
        :return:  BulkIssuanceResponse object of the updated  country
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.bulkissuances.BulkIssuancesCollection>'
