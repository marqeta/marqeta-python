from marqeta.resources.collection import Collection
from marqeta.response_models.real_time_fee_group import RealTimeFeeGroup


class RealTimeFeeGroupsCollection(object):
    _endpoint = 'realtimefeegroups'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, RealTimeFeeGroup)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the realtimefeegroups  Returns list of all realtimefeegroups object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a realtimefeegroups with the specified data
            Returns the card product object which has created realtimefeegroups information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the realtimefeegroups information for the requested token
            Returns the cardproduct object which has realtimefeegroups information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the realtimefeegroups information for the requested token  with the data
                Returns the realtimefeegroups object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.realtimefeegroups.RealTimeFeeGroupsCollection>'
