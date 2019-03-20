
from marqeta.resources.collection import Collection
from marqeta.response_models.commando_mode_response import CommandoModeResponse
from marqeta.response_models.commando_mode_transition_response import CommandoModeTransitionResponse
class CommandomodesCollection(object):

    _endpoint = 'commandomodes'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CommandoModeResponse)

    def __call__(self, token):
        return CommandomodesContext(token, self.client)

    def stream(self, params = None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the commandomodes  Returns list of all commandomodes object '''
    def list(self, params=None, limit = float('inf')):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Finds the commandomodes information for the requested token
            Returns the cardproduct object which has commandomodes information '''
    def find(self, token, params=None):
        return self.collections.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.commandomodes.Commandomodes>'


class CommandomodesContext(CommandomodesCollection):

    def __init__(self, token, client):
        super(CommandomodesContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client, CommandoModeTransitionResponse))

    class Transitions(object):

        _endpoint = 'commandomodes'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None,limit=float('inf')):
            return self.collection.list(endpoint=self._endpoint+'/{}/transitions'.format(self.token),query_params=params,
                                        limit = limit)

        def create(self, data):
            return self.collection.create(data,
                                          endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint=self._endpoint+'/transitions/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.commandomodes.CommandomodesContext.Transitions>'
