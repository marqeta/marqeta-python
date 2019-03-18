from marqeta.resources.collection import Collection
from marqeta.response_models.merchant_response_model import MerchantResponseModel
from marqeta.response_models.store_response_model import StoreResponseModel


class MerchantsCollection(object):
    _endpoint = 'merchants'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, MerchantResponseModel)

    def __call__(self, token):
        return MerchantContext(token, self.client)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the merchants  Returns list of all merchants object '''

    def list(self, params=None, limit=float('inf')):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a merchants with the specified data
            Returns the card product object which has created merchants information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the merchants information for the requested token
            Returns the cardproduct object which has merchants information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the merchants information for the requested token  with the data
                Returns the merchants object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.merchants.MerchantsCollection>'


class MerchantContext(MerchantsCollection):

    def __init__(self, token, client):
        super(MerchantContext, self).__init__(client)
        self.token = token
        self.stores = self.Stores(self.token, Collection(client, StoreResponseModel))

    class Stores(object):
        _endpoint = 'merchants/{}/stores'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params=None, limit=float('inf')):
            return self.collection.list(endpoint=self._endpoint.format(self.token), query_params=params,
                                        limit=limit)

    def __repr__(self):
        return '<<Marqeta.resources.merchants.MerchantContext>'
