from marqeta.resources.collection import Collection
from marqeta.response_models.control_token_response import ControlTokenResponse


class PinsCollection(object):
    _endpoint = 'pins'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, ControlTokenResponse)

    def new(self, data):
        return self.collections.create(endpoint=self._endpoint, data=data)

    ''' Lists all the offers  Returns list of all offers object '''

    def create_control_token(self, data):
        return self.collections.save(endpoint=self._endpoint + '/controltoken', data=data)

    def __repr__(self):
        return '<Marqeta.resources.pins.PinsCollection>'
