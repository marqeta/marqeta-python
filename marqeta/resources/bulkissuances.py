from marqeta.resources.collection import Collection
from marqeta.response_models.bulk_issuance_response import BulkIssuanceResponse


class BulkissuancesCollection(object):
    _endpoint = 'bulkissuances'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, BulkIssuanceResponse)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the bulkissuances  Returns list of all bulkissuances object '''

    def list(self, params=None, limit=float('inf')):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a bulkissuances with the specified data
            Returns the card product object which has created bulkissuances information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the bulkissuances information for the requested token
            Returns the cardproduct object which has bulkissuances information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the bulkissuances information for the requested token  with the data
                Returns the bulkissuances object which has updated user information'''

    def __repr__(self):
        return '<Marqeta.resources.bulkissuances.Bulkissuances>'
