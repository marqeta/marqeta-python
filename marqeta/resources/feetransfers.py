#!/usr/bin/env python3

'''FEETRANSFERS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.fee_transfer_response import FeeTransferResponse


class FeeTransfersCollection(object):
    '''
    Marqeta API 'feetransfers' endpoint list, create, find and update operations
    '''
    _endpoint = 'feetransfers'

    def __init__(self, client):
        '''
        Creates a client collection objects
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, FeeTransferResponse)

    def create(self, data, params=None):
        '''
        Creates an feetransfers object
        :param data: data required for creation
        :param params: query parameters
        :return: FeeTransferResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params,
                                       data=data)

    def find(self, token, params=None):
        '''
        Finds a specific feetransfers object
        :param token: feetransfers token
        :param params: query parameters
        :return: FeeTransferResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.feetransfers.FeeTransfersCollection>'
