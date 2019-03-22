from marqeta.resources.collection import Collection
from marqeta.response_models.campaign_response_model import CampaignResponseModel
from marqeta.response_models.store_model import StoreModel


class CampaignsCollection(object):
    _endpoint = 'campaigns'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CampaignResponseModel)

    def __call__(self, token):
        return CampaignsContext(token, self.client)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the campaigns  Returns list of all campaigns object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a campaigns with the specified data
            Returns the card product object which has created campaigns information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the campaigns information for the requested token
            Returns the cardproduct object which has campaigns information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the campaigns information for the requested token  with the data
                Returns the campaigns object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.campaigns.CampaignsCollection>'


class CampaignsContext(CampaignsCollection):

    def __init__(self, token, client):
        super(CampaignsContext, self).__init__(client)
        self.token = token
        self.stores = self.Stores(self.token, Collection(client, StoreModel))

    class Stores(object):
        _endpoint = 'campaigns/{}/stores'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint.format(self.token), query_params=params,
                                        limit=limit)

    def __repr__(self):
        return '<Marqeta.resources.campaigns.CampaignsContext.Stores>'
