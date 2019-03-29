#!/usr/bin/env python3

'''MCCGROUPS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.mcc_group_model import MccGroupModel


class MccGroupsCollection(object):
    '''
      Marqeta API 'mccgroups' endpoint list, create, find and update operations
    '''
    _endpoint = 'mccgroups'

    def __init__(self, client):
        '''
        Creates a client collection objects
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, MccGroupModel)

    def page(self, params=None):
        '''
        Provides the requested page for mccgroups
        :param params: query parameters
        :return: requested page with MccGroupModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: MccGroupModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the mccgroups
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of MccGroupModel object:
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an mccgroups object
        :param data: data required for creation
        :param params: query parameters
        :return: MccGroupModel object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)


    def find(self, token, params=None):
        '''
        Finds a specific mccgroups object
        :param token: mccgroups token
        :param params: query parameters
        :return: MccGroupModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an mccgroups object
        :param token: mccgroups token
        :param data: data to be updated
        :return: MccGroupModel object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.mccgroups.MccGroupsCollection>'
