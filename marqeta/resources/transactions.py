from marqeta.resources.collection import Collection
from marqeta.response_models.transaction_model import TransactionModel


class TransactionsCollection(object):
    _endpoint = 'transactions'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, TransactionModel)

    def __call__(self, token):
        return TranscationContext(token, self.client, self.collections)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the transactions  Returns list of all transactions object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a transactions with the specified data
            Returns the card product object which has created transactions information'''

    def stream_for_funding_source(self, token, params=None):
        return self.collections.stream(endpoint=self._endpoint + '/fundingsource/{}'.format(token), query_params=params)

    ''' Lists all the transactions  Returns list of all transactions object '''

    def list_for_funding_source(self, token, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint + '/fundingsource/{}'.format(token), query_params=params,
                                     limit=limit)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.transactions.Transactions>'


class TranscationContext(TransactionsCollection):

    def __init__(self, token, client, collections):
        super(TranscationContext, self).__init__(client)
        self.token = token
        self.related = self.Related(self.token, collections)

    class Related(object):
        _endpoint = 'transactions/{}/related'

        def __init__(self, token, collections):
            self.token = token
            self.collections = collections

        def stream(self, params=None):
            return self.collections.stream(endpoint=self._endpoint.format(self.token), query_params=params)

        ''' Lists all the transactions  Returns list of all transactions object '''

        def list(self, params=None, limit=None):
            return self.collections.list(endpoint=self._endpoint.format(self.token), query_params=params, limit=limit)
