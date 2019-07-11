
'''DIGITALWALLETTOKENS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.digital_wallet_token import DigitalWalletToken
from marqeta.response_models.digital_wallet_token_transition_response import DigitalWalletTokenTransitionResponse


class DigitalWalletTokensCollection(object):
    '''
    Marqeta API 'digitalwallettokens' endpoint list, create, find and update operations
    '''

    _endpoint = 'digitalwallettokens'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, DigitalWalletToken)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: digitalwallettokens token
        :return: DigitalWalletTokensContext object
        '''
        return DigitalWalletTokensContext(token, self.client)
    def page(self, count=5, start_index=0, params=None):
        '''
        Provides the requested page for digitalwallettokens
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with DigitalWalletToken object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: DigitalWalletToken object
        '''
        query_params = {'sort_by': '-createdTime', 'count':10}
        if params is not None:
            query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint, query_params=query_params)

    def list(self, params=None, limit=None):
        '''
        List all the digitalwallettokens
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of DigitalWalletToken object:
        '''
        query_params = {'sort_by': '-createdTime', 'count':10}
        if params is not None:
            query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=query_params, limit=limit)


    def page_for_card(self, user_token, count=5, start_index=0, params=None):
        '''
        Provides the requested page for card
        :param user_token:
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with DigitalWalletToken object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + "/card/{}".format(user_token),
                                     count=count, start_index=start_index, query_params=params)

    def stream_for_card(self, user_token, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param user_token:
        :param params: query parameters
        :return: DigitalWalletToken object
        '''
        return self.collections.stream(endpoint=self._endpoint + "/card/{}".format(user_token),
                                       query_params=params)

    def list_for_card(self, user_token, params=None, limit=None):
        '''
        List all the cards for the user
        :param user_token:
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of DigitalWalletToken object
        '''
        return self.collections.list(endpoint=self._endpoint + "/card/{}".format(user_token),
                                     query_params=params,
                                     limit=limit)
    def find(self, token, params=None):
        '''
        Finds a specific digitalwallettokens object
        :param token: digitalwallettokens token
        :param params: query parameters
        :return: DigitalWalletToken object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def find_show_pan(self, card_token, params=None):
        '''
        Finds a specific pan object for card
        :param card_token: card token
        :param params: query parameters
        :return: DigitalWalletToken objec
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}/showtokenpan'.
                                     format(card_token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.digitalwallettokens.DigitalWalletTokensCollection>'


class DigitalWalletTokensContext(DigitalWalletTokensCollection):
    ''' class to specify sub endpoints for digitalwallettokens '''

    def __init__(self, token, client):

        super(DigitalWalletTokensContext, self).__init__(client)

        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client,
                                                                   DigitalWalletTokenTransitionResponse))
    class Transitions(object):
        '''
        Lists, Creates and Finds the notes for digitalwallettokens
        Returns DigitalWalletTokenTransitionResponse object
        '''
        _endpoint = 'digitalwallettokentransitions'
    
        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(count=count, start_index=start_index, query_params=params,
                                        endpoint=self._endpoint + '/digitalwallettoken/{}'.
                                        format(self.token))

        def stream(self, params=None):
            query_params = {'sort_by': '-id'}
            if params is not None:
                query_params.update(params)
            return self.collection.stream(query_params=query_params,
                                        endpoint=self._endpoint + '/digitalwallettoken/{}'.
                                        format(self.token))

        def list(self, params=None, limit=None):
            query_params = {'sort_by': '-id'}
            if params is not None:
                query_params.update(params)
            return self.collection.list(query_params=query_params,
                                        endpoint=self._endpoint + '/digitalwallettoken/{}'.
                                        format(self.token), limit=limit)
            
        def create(self, data, params=None):
            return self.collection.create(endpoint=self._endpoint, query_params=params, data=data)

        def find(self, token, params=None):
            return self.collection.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)


        def __repr__(self):
           return '<Marqeta.resources.digitalwallettokens.DigitalWalletTokensContext.Transitions>'

    def __repr__(self):
        return '<Marqeta.resources.digitalwallettokens.DigitalWalletTokensContext>'


