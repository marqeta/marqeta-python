
from marqeta.resources.collection import Collection
from marqeta.response_models.deposit_deposit_response import DepositDepositResponse
from marqeta.response_models.deposit_account import DepositAccount
from marqeta.response_models.direct_deposit_transition_response import DirectDepositTransitionResponse

class DirectdepositsCollection(object):

    _endpoint = 'directdeposits'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, DepositDepositResponse)
        self.accounts = Accounts(Collection(self.client, DepositAccount))

    def __call__(self, token):
        return DirectdepositsContext(token, self.client)

    def stream(self, params = None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the directdeposits  Returns list of all directdeposits object '''
    def list(self, params=None, limit = float('inf')):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Finds the directdeposits information for the requested token
            Returns the cardproduct object which has directdeposits information '''
    def find(self, token, params=None):
        return self.collections.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)


    def __repr__(self):
        return '<Marqeta.resources.directdeposits.Directdeposits>'


class Accounts(object):

    _endpoint = 'directdeposits/accounts'

    def __init__(self, collection):
        self.collections = collection

    def find(self, token, params=None):
        return self.collections.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint+'/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.directdeposits.Accounts>'


class DirectdepositsContext(DirectdepositsCollection):

    def __init__(self, token, client):
        super(DirectdepositsContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client, DirectDepositTransitionResponse))


    class Transitions(object):

        _endpoint = 'directdeposits/transitions'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def stream(self, params= None,limit=float('inf')):
            query_params = {'sort_by': '-id', 'count': 5, 'start_index': 0}
            if params is not None:
                query_params.update(params)
            return self.collection.stream(endpoint=self._endpoint,query_params=query_params,
                                        limit = limit)

        def list(self, params= None,limit=float('inf')):
            query_params = {'sort_by': '-id', 'count': 5, 'start_index': 0}
            if params is not None:
                query_params.update(params)
            return self.collection.list(endpoint=self._endpoint,query_params=query_params,
                                        limit = limit)

        def create(self, data):
            return self.collection.create(data,
                                          endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint=self._endpoint+'/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.directdeposit.DirectdepositsContext.Transitions>'
