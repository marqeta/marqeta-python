from marqeta.resources.collection import Collection
from marqeta.response_models.msa_order_response import MsaOrderResponse
from marqeta.response_models.msa_returns import MsaReturns


class MsaordersCollection(object):
    _endpoint = 'msaorders'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, MsaOrderResponse)
        self.unloads = MsaordersUnloadsCollection(Collection(self.client, MsaReturns))

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the msaorders information for the requested token
            Returns the cardproduct object which has msaorders information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the msaorders information for the requested token  with the data
                Returns the msaorders object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.msaorders.Msaorders>'


class MsaordersUnloadsCollection(object):
    _endpoint = 'msaorders/unloads'

    def __init__(self, collection):
        self.collections = collection

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the msaorders/unloads  Returns list of all msaorders/unloads object '''

    def list(self, params=None, limit=float('inf')):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a msaorders/unloads with the specified data
            Returns the card product object which has created msaorders/unloads information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the msaorders/unloads information for the requested token
            Returns the cardproduct object which has msaorders/unloads information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.msaorders_unloads.MsaordersUnloads>'
