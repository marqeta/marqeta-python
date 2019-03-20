from marqeta.resources.collection import Collection
from marqeta.response_models.cardholder_balances import CardholderBalances


class BalancesTokenCollection(object):
    _endpoint = 'balances'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CardholderBalances)

    def stream_msas_for_user_or_business(self, token, params=None):
        return self.collections.stream(endpoint=self._endpoint+'/{}/msas'.format(token), query_params=params)

    ''' Lists all the balances/{token}  Returns list of all balances/{token} object '''

    def list_msas_for_user_or_business(self, token, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint+'/{}/msas'.format(token), query_params=params, limit=limit)

    ''' Finds the balances/{token} information for the requested token
            Returns the cardproduct object which has balances/{token} information '''

    def find_for_user_or_business(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint+'/{}'.format(token), query_params=params)

    ''' Update the balances/{token} information for the requested token  with the data
                Returns the balances/{token} object which has updated user information'''

    def __repr__(self):
        return '<Marqeta.resources.balances_token.BalancesToken>'
