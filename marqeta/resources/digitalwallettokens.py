from marqeta.resources.collection import Collection

from marqeta.response_models.digital_wallet_token_transition_response import DigitalWalletTokenTransitionResponse
from marqeta.response_models.digital_wallet_token import DigitalWalletToken


class DigitalWalletTokensCollection(object):
    _endpoint = 'digitalwallettokens'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, DigitalWalletToken)

    def __call__(self, token):
        return DigitalContext(token, self.client)

    def page(self, params={}):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    ''' Iterates through cards based on last_four number
        returns card object one at a time'''

    def stream(self, params={}):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the cards Returns list of all card object based on last_four number of card'''

    def list(self, params={}, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def page_for_card(self, user_token, params=None):
        return self.collections.page(endpoint=self._endpoint + "/card/{}".format(user_token), query_params=params)

    def stream_for_card(self, user_token, params=None):
        return self.collections.stream(endpoint=self._endpoint + "/card/{}".format(user_token), query_params=params)

    ''' Lists all the cards Returns list of all card object based on user token '''

    def list_for_card(self, user_token, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint + "/card/{}".format(user_token), query_params=params,
                                     limit=limit)

    def find(self, card_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(card_token), query_params=params)

    ''' Finds the card number information for the requested card token
                Returns the card object which has card number '''

    def find_show_pan(self, card_token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}/showtokenpan'.format(card_token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.digitalwallettokens.DigitalwallettokensCollection>'


class DigitalContext(DigitalWalletTokensCollection):

    def __init__(self, token, client):
        super(DigitalContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client, DigitalWalletTokenTransitionResponse))

    ''' list, create and find operations for cards transition'''

    class Transitions(object):
        _endpoint = 'digitalwallettokentransitions'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, params=None):
            return self.collection.page(query_params=params,
                                        endpoint=self._endpoint + '/digitalwallettoken/{}'.format(self.token))

        def stream(self, params=None):
            return self.collection.stream(query_params=params,
                                          endpoint=self._endpoint + '/digitalwallettoken/{}'.format(self.token))

        def list(self, params=None, limit=None):
            return self.collection.list(query_params=params,
                                        endpoint=self._endpoint + '/digitalwallettoken/{}'.format(self.token),
                                        limit=limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(endpoint=self._endpoint + '/{}'.format(transition_token))

    def __repr__(self):
        return '<Marqeta.resources.digitalwallettokens.DigitalContext.Transitions>'
