from marqeta.resources.collection import Collection
from marqeta.response_models.account_holder_group_response import AccountHolderGroupResponse


class AccountholdergroupsCollection(object):
    _endpoint = 'accountholdergroups'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, AccountHolderGroupResponse)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the accountholdergroups  Returns list of all accountholdergroups object '''

    def list(self, params=None, limit=float('inf')):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 10, 'start_index': 0}
        if params is not None:
            query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=query_params, limit=limit)

    ''' Create a accountholdergroups with the specified data
            Returns the card product object which has created accountholdergroups information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the accountholdergroups information for the requested token
            Returns the cardproduct object which has accountholdergroups information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the accountholdergroups information for the requested token  with the data
                Returns the accountholdergroups object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.accountholdergroups.Accountholdergroups>'
