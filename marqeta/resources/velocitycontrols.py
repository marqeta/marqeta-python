from marqeta.resources.collection import Collection
from marqeta.response_models.velocity_control_response import VelocityControlResponse


class VelocityControlsCollection(object):
    _endpoint = 'velocitycontrols'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, VelocityControlResponse)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def page_available_for_user(self, token, params=None):
        return self.collections.page(endpoint=self._endpoint + '/user/{}/available'.format(token),
                                     query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def stream_available_for_user(self, token, params=None):
        return self.collections.stream(endpoint=self._endpoint + '/user/{}/available'.format(token),
                                       query_params=params)

    ''' Lists all the velocitycontrols  Returns list of all velocitycontrols object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Lists all the velocitycontrols  Returns list of all velocitycontrols object '''

    def list_available_for_user(self, token, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint + '/user/{}/available'.format(token), query_params=params,
                                     limit=limit)

    ''' Create a velocitycontrols with the specified data
            Returns the card product object which has created velocitycontrols information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the velocitycontrols information for the requested token
            Returns the cardproduct object which has velocitycontrols information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the velocitycontrols information for the requested token  with the data
                Returns the velocitycontrols object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.velocitycontrols.VelocityControlsCollection>'
