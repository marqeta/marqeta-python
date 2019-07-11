
'''CHARGEBACKS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.chargeback_response import ChargebackResponse
from marqeta.response_models.chargeback_transition_response import ChargebackTransitionResponse


class ChargebacksCollection(object):
    '''
    Marqeta API 'chargebacks' endpoint list, create, find and update operations
    '''

    _endpoint = 'chargebacks'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, ChargebackResponse)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: chargebacks token
        :return: ChargebacksContext object
        '''
        return ChargebacksContext(token, self.client)
    def page(self, count=5, start_index=0, params=None):
        '''
        Provides the requested page for chargebacks
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with ChargebackResponse object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: ChargebackResponse object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the chargebacks
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of ChargebackResponse object:
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an chargebacks object
        :param data: data required for creation
        :param params: query parameters
        :return: ChargebackResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)
    def find(self, token, params=None):
        '''
        Finds a specific chargebacks object
        :param token: chargebacks token
        :param params: query parameters
        :return: ChargebackResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)
    def __repr__(self):
        return '<Marqeta.resources.chargebacks.ChargebacksCollection>'


class ChargebacksContext(ChargebacksCollection):
    ''' class to specify sub endpoints for chargebacks '''

    def __init__(self, token, client):

        super(ChargebacksContext, self).__init__(client)

        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client,
                                                                   ChargebackTransitionResponse))
    def grant_provisional_credit(self):
        return self.client.put('chargebacks/{}/grantprovisionalcredit'.format(self.token),
                               data={})[0]

    def reverse_provisional_credit(self):
        return self.client.put('chargebacks/{}/reverseprovisionalcredit'.format(self.token),
                               data={})[0]

    class Transitions(object):
        '''
        Lists, Creates and Finds the notes for chargebacks
        Returns ChargebackTransitionResponse object
        '''

        _endpoint = 'chargebacks'
    
        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(endpoint=self._endpoint + '/{}/transitions'.
                                        format(self.token), count=count, start_index=start_index,
                                        query_params=params)

        def stream(self, params=None):
            return self.collection.stream(endpoint=self._endpoint + '/{}/transitions'.
                                          format(self.token), query_params=params)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint + '/{}/transitions'.
                                        format(self.token), query_params=params, limit=limit)
        def create(self, data):
            return self.collection.create(data,
                                          endpoint=self._endpoint + '/transitions')

        def find(self, transition_token):
            return self.collection.find(
                endpoint=self._endpoint + '/transitions/{}'.format(transition_token))


        def __repr__(self):
           return '<Marqeta.resources.chargebacks.ChargebacksContext.Transitions>'

    def __repr__(self):
        return '<Marqeta.resources.chargebacks.ChargebacksContext>'


