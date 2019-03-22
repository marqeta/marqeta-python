from marqeta.resources.collection import Collection
from marqeta.response_models.offer_response_model import OfferResponseModel


class OffersCollection(object):
    _endpoint = 'offers'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, OfferResponseModel)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the offers  Returns list of all offers object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a offers with the specified data
            Returns the card product object which has created offers information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the offers information for the requested token
            Returns the cardproduct object which has offers information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the offers information for the requested token  with the data
                Returns the offers object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.offers.OffersCollection>'
