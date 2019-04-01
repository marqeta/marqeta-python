#!/usr/bin/env python3

'''COMMONDOMODES RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.commando_mode_response import CommandoModeResponse
from marqeta.response_models.commando_mode_transition_response import CommandoModeTransitionResponse


class CommandoModesCollection(object):
    '''
    Marqeta API 'commandomodes' endpoint list, create, find and update operations
    '''
    _endpoint = 'commandomodes'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, CommandoModeResponse)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: commandomodes token
        :return: CommandoModesContext object
        '''
        return CommandoModesContext(token, self.client)

    def page(self, count=5, start_index=0):
        '''
        Provides the requested page for commandomodes
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with CommandoModeResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: CommandoModeResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''

        List all the commandomodes
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of CommandoModeResponse object:
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def find(self, token, params=None):
        '''
        Finds a specific commandomodes object
        :param token: commandomodes token
        :param params: query parameters
        :return: CommandoModeResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.commandomodes.CommandoModesCollection>'


class CommandoModesContext(CommandoModesCollection):
    ''' class to specify sub endpoints for commandomodes '''

    def __init__(self, token, client):
        super(CommandoModesContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client,
                                                                   CommandoModeTransitionResponse))

    class Transitions(object):
        '''
        Lists, Creates and Finds the notes for commandomodes
        Returns CommandoModeTransitionResponse object
        '''

        _endpoint = 'commandomodes'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0):
            return self.collection.page(endpoint=self._endpoint + '/{}/transitions'.
                                        format(self.token), count=count, start_index=start_index)

        def stream(self, params=None):
            return self.collection.stream(endpoint=self._endpoint + '/{}/transitions'.
                                          format(self.token), query_params=params)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint + '/{}/transitions'.
                                        format(self.token), query_params=params, limit=limit)

        def create(self, data):
            return self.collection.create(data,
                                          endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                endpoint=self._endpoint + '/transitions/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.commandomodes.CommandomodesContext.Transitions>'

    def __repr__(self):
        return '<Marqeta.resources.commandomodes.CommandoModesContext>'
