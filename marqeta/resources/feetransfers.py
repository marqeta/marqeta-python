from marqeta.resources.collection import Collection
from marqeta.response_models.fee_transfer_response import FeeTransferResponse


class FeeTransfersCollection(object):

    _endpoint = 'feetransfers'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, FeeTransferResponse)

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the feetransfers information for the requested token
            Returns the cardproduct object which has feetransfers information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.feetransfers.Feetransfers>'
