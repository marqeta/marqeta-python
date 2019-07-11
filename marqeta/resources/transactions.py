
'''TRANSACTIONS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.transaction_model import TransactionModel


class TransactionsCollection(object):
    '''
    Marqeta API 'transactions' endpoint list, create, find and update operations
    '''

    _endpoint = 'transactions'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, TransactionModel)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: transactions token
        :return: TransactionsContext object
        '''

        return TransactionsContext(token, self.client, self.collections)

    def page(self, params=None, count=5, start_index=0):
        '''
        Provides the requested page for transactions
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with TransactionModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: TransactionModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''

        List all the transactions
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of TransactionModel object:
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)


    def page_for_funding_source(self, token, count=5, start_index=0, params=None):
        '''
        Provides the requested page for transactions for specified funding source
       :param count: data to be displayed per page
        :param start_index: start_index
        :param token: funding source token
        :return: requested page with TransactionModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + '/fundingsource/{}'.format(token),
                                     count=count, start_index=start_index)

    def stream_for_funding_source(self, token, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param token: funding source token
        :param params: query parameters
        :return: TransactionModel object
        '''
        return self.collections.stream(endpoint=self._endpoint + '/fundingsource/{}'.format(token),
                                       query_params=params)

    def list_for_funding_source(self, token, params=None, limit=None):
        '''
        List all the transactions for specified funding source
        :param token: funding source token
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of TransactionModel object
        '''
        return self.collections.list(endpoint=self._endpoint + '/fundingsource/{}'.format(token),
                                     query_params=params, limit=limit)
    def find(self, token, params=None):
        '''
        Finds a specific transactions object
        :param token: transactions token
        :param params: query parameters
        :return: TransactionModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)
    def __repr__(self):
        return '<Marqeta.resources.transactions.TransactionsCollection>'


class TransactionsContext(TransactionsCollection):

    ''' class to specify sub endpoints for transactions '''
    def __init__(self, token, client, collection):
        super(TransactionsContext, self).__init__(client)
        self.token = token
        self.related = self.Related(self.token, collection)

    class Related(object):
        '''
        Lists the transactions related to specifies transaction
        Return TransactionModel object
        '''
        _endpoint = 'transactions/{}/related'
        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(endpoint=self._endpoint.format(self.token),
                                        count=count, start_index=start_index, query_params=params)

        def stream(self, params=None):
            return self.collection.stream(endpoint=self._endpoint.format(self.token),
                                          query_params=params)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint.format(self.token),
                                        query_params=params, limit=limit)


        def __repr__(self):
            return '<Marqeta.resources.transactions.TransactionsContext.Transitions>'

    def __repr__(self):
        return '<Marqeta.resources.transactions.TransactionsContext>'


