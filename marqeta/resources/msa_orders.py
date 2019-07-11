
'''MSAORDERS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.msa_order_response import MsaOrderResponse
from marqeta.response_models.msa_returns import MsaReturns

class MsaOrdersCollection(object):
    '''
    Marqeta API 'msaorders' endpoint list, create, find and update operations
    '''

    _endpoint = 'msaorders'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, MsaOrderResponse)
        self.unloads = Unloads(Collection(self.client, MsaReturns))

    def create(self, data, params=None):
        '''
        Creates an msaorders object
        :param data: data required for creation
        :param params: query parameters
        :return: MsaOrderResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, data=data, query_params=params )

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


class Unloads(object):
    '''
    Lists, Creates and Finds the msaorders unloads
    Returns MsaReturns object
    '''
    _endpoint = 'msaorders/unloads'

    def __init__(self, collection):
        self.collections = collection

    def page(self, count=5, start_index=0, params=None):
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index,
                                     query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.msaorders.Unloads>'
