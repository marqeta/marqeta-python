
'''CARDS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.card_response import CardResponse
from marqeta.response_models.card_transition_response import CardTransitionResponse
from marqeta.response_models.pan_response import PanResponse


class CardsCollection(object):
    '''
    Marqeta API 'cards' endpoint list, create, find and update operations
    '''

    _endpoint = 'cards'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, CardResponse)
        self.collections_pan_response = Collection(self.client, PanResponse)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: cards token
        :return: CardsContext object
        '''
        return CardsContext(token, self.client)

    def page(self, last_four, params={}, count=5, start_index=0):
        '''
        Provides the requested page for cards
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with CardResponse object for the requested
        page 'data'field
        '''
        params['last_four'] = last_four
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index, query_params=params)

    def stream(self, last_four, params={}):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: CardResponse object
        '''
        params['last_four'] = last_four
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, last_four, params={}, limit=None):
        '''

        List all the cards
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of CardResponse object:
        '''
        params['last_four'] = last_four
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)



    def page_for_user(self, user_token, count=5, start_index=0, params=None):
        '''
        Provides the requested page for cards
        :param user_token: user token
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with CardResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint + "/user/{}".
                                     format(user_token), count=count, start_index=start_index,
                                     query_params=params)

    def stream_for_user(self, user_token, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param user_token: user token
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint + "/user/{}".
                                       format(user_token), query_params=params)

    def list_for_user(self, user_token, params=None, limit=None):
        '''
        List all the cards
        :param params: query parameters
        :param limit: parameter to limit the list count
        :param user_token:
        :param params:
        :return: List of CardResponse object:
        '''
        return self.collections.list(endpoint=self._endpoint + "/user/{}".
                                     format(user_token), query_params=params,
                                     limit=limit)

    def create(self, data={}, params=None):
        '''
        Creates an cards object
        :param data: data required for creation
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)
    def find(self, token, params=None):
        '''
        Finds a specific cards object
        :param token: cards token
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def find_show_pan(self, card_token, params=None):
        '''
        Finds a specific cards object
        :param card_token: cards token
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}/showpan'.
                                     format(card_token), query_params=params)

    def find_by_barcode(self, barcode, params=None):
        '''
        Finds a specific cards object
        :param barcode: card barcode
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/barcode/{}'.
                                     format(barcode), query_params=params)
    def find_for_merchant(self, token, params=None):
        '''
        Finds a specific cards object
        :param token: merchant token
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/merchant/{}'.
                                     format(token), query_params=params)

    def find_for_merchant_show_pan(self, token, params=None):
        '''
        Finds a specific cards object
        :param token: merchant token
        :param params: query parameters
        :return: CardResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/merchant/{}/showpan'.
                                     format(token), query_params=params)

    def create_for_merchant(self, token, data):
        '''
        Creates an cards object
        :param data: data required for creation
        :param params: query parameters
        :param token: merchant token
        :return: CardResponse object
        '''
        return self.collections.create(endpoint=self._endpoint + '/merchant/{}'.
                                       format(token), data=data)

    def tokens_for_pan(self, pan_token):
        '''
        Creates token for pan
        :param pan_token: pan token
        :return: PanResponse object
        '''
        pan = {'pan': pan_token}
        return self.collections_pan_response.create(endpoint=self._endpoint + '/getbypan', data=pan)


    def save(self, token, data):
        '''
        Updates an cards  object
        :param token: cards  token
        :param data: data to be updated
        :return: CardResponse object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))
    def __repr__(self):
        return '<Marqeta.resources.cards.CardsCollection>'


class CardsContext(CardsCollection):

    ''' class to specify sub endpoints for cards '''
    def __init__(self, token, client):
        super(CardsContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client,
                                                                   CardTransitionResponse))

    class Transitions(object):
        '''
        Lists, Creates and Finds the notes for cards
        Returns CardTransitionResponse object
        '''

        _endpoint = 'cardtransitions'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(count=count, start_index=start_index, query_params=params,
                                        endpoint=self._endpoint + '/card/{}'.format(self.token))

        def stream(self, params=None):
            return self.collection.stream(query_params=params,
                                          endpoint=self._endpoint + '/card/{}'.format(self.token))

        def list(self, params=None, limit=None):
            return self.collection.list(query_params=params,
                                        endpoint=self._endpoint + '/card/{}'.format(self.token),
                                        limit=limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(endpoint=self._endpoint + '/{}'.format(transition_token))


        def __repr__(self):
            return '<Marqeta.resources.cards.CardsContext.Transitions>'

    def __repr__(self):
        return '<Marqeta.resources.cards.CardsContext>'


