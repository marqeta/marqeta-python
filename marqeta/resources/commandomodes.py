from marqeta.resources.collection import Collection
from marqeta.response_models.commando_mode_response import CommandoModeResponse
from marqeta.response_models.commando_mode_transition_response import CommandoModeTransitionResponse


class CommandoModesCollection(object):
    _endpoint = 'commandomodes'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CommandoModeResponse)

    def __call__(self, token):
        return CommandoModesContext(token, self.client)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the commandomodes  Returns list of all commandomodes object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Finds the commandomodes information for the requested token
            Returns the cardproduct object which has commandomodes information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.commandomodes.CommandoModesCollection>'


class CommandoModesContext(CommandoModesCollection):

    def __init__(self, token, client):
        super(CommandoModesContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client, CommandoModeTransitionResponse))

    class Transitions(object):
        _endpoint = 'commandomodes'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, params=None):
            return self.collection.page(endpoint=self._endpoint + '/{}/transitions'.format(self.token),
                                        query_params=params)

        def stream(self, params=None):
            return self.collection.stream(endpoint=self._endpoint + '/{}/transitions'.format(self.token),
                                          query_params=params)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint + '/{}/transitions'.format(self.token),
                                        query_params=params,
                                        limit=limit)

        def create(self, data):
            return self.collection.create(data,
                                          endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                endpoint=self._endpoint + '/transitions/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.commandomodes.CommandomodesContext.Transitions>'
