from marqeta.resources.collection import Collection
from marqeta.response_models.chargeback_response import ChargebackResponse
from marqeta.response_models.chargeback_transition_response import ChargebackTransitionResponse


class ChargebacksCollection(object):
    _endpoint = 'chargebacks'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, ChargebackResponse)

    def __call__(self, token):
        return ChargeBackContext(token, self.client)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the chargebacks  Returns list of all chargebacks object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a chargebacks with the specified data
            Returns the card product object which has created chargebacks information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the chargebacks information for the requested token
            Returns the cardproduct object which has chargebacks information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the chargebacks information for the requested token  with the data
                Returns the chargebacks object which has updated user information'''

    def __repr__(self):
        return '<Marqeta.resources.chargebacks.ChargebacksCollection>'


class ChargeBackContext(ChargebacksCollection):

    def __init__(self, token, client):
        super(ChargeBackContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client, ChargebackTransitionResponse))

    def grant_provisional_credit(self):
        return self.client.put('chargebacks/{}/grantprovisionalcredit'.format(self.token), data={})[0]

    def reverse_provisional_credit(self):
        return self.client.put('chargebacks/{}/reverseprovisionalcredit'.format(self.token), data={})[0]

    ''' list, create and find operations for cards transition'''

    class Transitions(object):
        _endpoint = 'chargebacks'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, params=None):
            return self.collection.page(query_params=params,
                                        endpoint=self._endpoint + '/{}/transitions'.format(self.token))

        def stream(self, params=None):
            return self.collection.stream(query_params=params,
                                          endpoint=self._endpoint + '/{}/transitions'.format(self.token))

        def list(self, params=None, limit=None):
            return self.collection.list(query_params=params,
                                        endpoint=self._endpoint + '/{}/transitions'.format(self.token), limit=limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint + '/transitions')

        def find(self, transition_token):
            return self.collection.find(endpoint=self._endpoint + '/transitions/{}'.format(transition_token))

    def __repr__(self):
        return '<Marqeta.resources.chargebacks.ChargeBackContext.Transitions>'
