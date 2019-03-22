from marqeta.resources.collection import Collection
from marqeta.response_models.offer_order_response import OfferOrderResponse


class OfferOrdersCollection(object):
    _endpoint = 'offerorders'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, OfferOrderResponse)

    ''' Create a offerorders with the specified data
            Returns the card product object which has created offerorders information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the offerorders information for the requested token
            Returns the cardproduct object which has offerorders information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.offerorders.OfferOrdersCollection>'
