from marqeta.resources.collection import Collection
from marqeta.response_models.mcc_group_model import MccGroupModel


class MccGroupsCollection(object):
    _endpoint = 'mccgroups'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, MccGroupModel)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the mccgroups  Returns list of all mccgroups object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a mccgroups with the specified data
            Returns the card product object which has created mccgroups information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the mccgroups information for the requested token
            Returns the cardproduct object which has mccgroups information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the mccgroups information for the requested token  with the data
                Returns the mccgroups object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.mccgroups.MccGroupsCollection>'
