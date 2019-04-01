#!/usr/bin/env python3

'''PROGRAMTRANSFER RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.program_transfer_response import ProgramTransferResponse
from marqeta.response_models.program_transfer_type_reponse import ProgramTransferTypeReponse


class ProgramTransfersCollection(object):
    '''
    Marqeta API 'programtransfers' endpoint list, create, find and update operations
    '''
    _endpoint = 'programtransfers'

    def __init__(self, client):
        '''
        Creates a client collection objects
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, ProgramTransferResponse)
        self.types = Types(Collection(client, ProgramTransferTypeReponse))

    def page(self, count=5, start_index=0, params=None):
        '''
        Provides the requested page for programtransfers
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with ProgramTransferResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: ProgramTransferResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the programtransfers
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of ProgramTransferResponse object
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an programtransfers object
        :param data: data required for creation
        :param params: query parameters
        :return: ProgramTransferResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific programtransfers object
        :param token: programtransfers token
        :param params: query parameters
        :return: ProgramTransferResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.programtransfers.ProgramTransfersCollection>'


class Types(object):
    ''' Lists, Creates, Update and Finds for ProgramTransfers Types
        Returns ProgramTransferTypeReponse object '''
    _endpoint = 'programtransfers/types'

    def __init__(self, collection):
        self.collections = collection

    def page(self, count=5, start_index=0, params=None):
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index,
                                     query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.programtransfers_types.ProgramtransfersTypes>'
