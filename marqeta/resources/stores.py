from marqeta.resources.collection import Collection
from marqeta.response_models.store_response_model import StoreResponseModel


class StoresCollection(object):
    _endpoint = 'stores'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, StoreResponseModel)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the stores  Returns list of all stores object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a stores with the specified data
            Returns the card product object which has created stores information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the stores information for the requested token
            Returns the cardproduct object which has stores information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def find_by_mid(self, mid_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/mid/{}'.format(mid_token), query_params=params)

    ''' Update the stores information for the requested token  with the data
                Returns the stores object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.stores.Stores>'
