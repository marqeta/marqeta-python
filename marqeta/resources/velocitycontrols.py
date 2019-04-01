#!/usr/bin/env python3
"""VELOCITY CONTROLS WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.velocity_control_response import VelocityControlResponse


class VelocityControlsCollection(object):
    '''
     Marqeta API 'velocitycontrols' endpoint list, create, find and update operations
    '''
    _endpoint = 'velocitycontrols'

    def __init__(self, client):
        '''
         Creates a client collection objects
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, VelocityControlResponse)

    def page(self, count=5, start_index=0, params=None):
        '''
        Provides the requested page for velocitycontrols
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with VelocityControlResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index,
                                     query_params=params)

    def page_available_for_user(self, token, count=5, start_index=0, params=None):
        '''
        Provides the requested page for velocitycontrols
        :param token: user token
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with VelocityControlResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + '/user/{}/available'.format(token),
                                     count=count, start_index=start_index, query_params=params)

    def stream(self, params=None):
        '''
         Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: VelocityControlResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def stream_available_for_user(self, token, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param token: user token
        :param params: query parameters
        :return: VelocityControlResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint + '/user/{}/available'.format(token),
                                       query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the velocitycontrols
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of VelocityControlResponse object
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def list_available_for_user(self, token, params=None, limit=None):
        '''
        Stream through the list of requested endpoint data field
        :param token: user token
        :param params: query parameters
        :return: VelocityControlResponse object
        '''
        return self.collections.list(endpoint=self._endpoint + '/user/{}/available'.format(token),
                                     query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an velocitycontrols object
        :param data: data required for creation
        :param params: query parameters
        :return: VelocityControlResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific velocitycontrols object
        :param token: velocitycontrols token
        :param params: query parameters
        :return: VelocityControlResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an velocitycontrols object
        :param token: velocitycontrols token
        :param data: data to be updated
        :return: VelocityControlResponse object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.velocitycontrols.VelocityControlsCollection>'
