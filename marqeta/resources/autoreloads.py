#!/usr/bin/env python3

from marqeta.resources.collection import Collection
from marqeta.response_models.auto_reload_response_model import AutoReloadResponseModel


class AutoReloadsCollection(object):
    '''
    Marqeta API 'autoreloads' endpoint list, create, find and update operations
    '''
    _endpoint = 'autoreloads'

    def __init__(self, client):
        '''
        Creates a client collection object
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, AutoReloadResponseModel)

    def page(self, params=None):
        '''
        Provides the requested page for autoreloads
        :param params: query parameters
        :return: requested page with AutoReloadResponseModel object for the requested
        page 'data'field
        '''
        query_params = {'count': 10}
        if params is not None:
            query_params.update(params)
        return self.collections.page(endpoint=self._endpoint, query_params=query_params)

    def stream(self, params=None):
        '''
         Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: AutoReloadResponseModel object
        '''
        query_params = {'count': 10}
        if params is not None:
            query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint, query_params=query_params)

    def list(self, params=None, limit=None):
        '''
        list all the autoreloads
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of AutoReloadResponseModel object
        '''
        query_params = {'count': 10}
        if params is not None:
            query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=query_params,
                                     limit=limit)

    def create(self, data):
        '''
        Creates an autoreloads object
        :param data: data required for creation
        :param params: query parameters
        :return: AutoReloadResponseModel object of the created country
        '''
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        '''
        Finds the existing country
        :param token: autoreloads token to find
        :param params: query parameters
        :return: AutoReloadResponseModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates the existing country data
        :param token: autoreloads token to update
        :param data: data to be updated
        :return:  AutoReloadResponseModel object of the updated  country
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.autoreloads.AutoReloadsCollection>'
