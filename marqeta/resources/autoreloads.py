from marqeta.resources.collection import Collection
from marqeta.response_models.auto_reload_response_model import AutoReloadResponseModel


class AutoReloadsCollection(object):
    _endpoint = 'autoreloads'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, AutoReloadResponseModel)

    def stream(self, params=None):
        query_params = {'count': 10}
        if params is not None:
            query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint, query_params=query_params)

    ''' Lists all the autoreloads  Returns list of all autoreloads object '''

    def list(self, params=None, limit=None):
        query_params = {'count': 10}
        if params is not None:
            query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=query_params, limit=limit)

    ''' Create a autoreloads with the specified data
            Returns the card product object which has created autoreloads information'''

    def create(self, data):
        return self.collections.create(endpoint=self._endpoint, data=data)

    ''' Finds the autoreloads information for the requested token
            Returns the cardproduct object which has autoreloads information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the autoreloads information for the requested token  with the data
                Returns the autoreloads object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.autoreloads.Autoreloads>'
