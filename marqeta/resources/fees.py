from marqeta.resources.collection import Collection
from marqeta.response_models.fee import Fee


class FeesCollection(object):
    _endpoint = 'fees'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, Fee)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the fees  Returns list of all fees object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a fees with the specified data
            Returns the card product object which has created fees information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the fees information for the requested token
            Returns the cardproduct object which has fees information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the fees information for the requested token  with the data
                Returns the fees object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.fees.Fees>'
