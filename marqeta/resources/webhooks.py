from marqeta.resources.collection import Collection
from marqeta.response_models.webhook_response_model import WebhookResponseModel
from marqeta.response_models.webhook_ping_model import WebhookPingModel


class WebhooksCollection(object):
    _endpoint = 'webhooks'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, WebhookResponseModel)

    def __call__(self, token):
        return WebhooksContext(token, self.client)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the webhooks  Returns list of all webhooks object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a webhooks with the specified data
            Returns the card product object which has created webhooks information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the webhooks information for the requested token
            Returns the cardproduct object which has webhooks information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the webhooks information for the requested token  with the data
                Returns the webhooks object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.webhooks.Webhooks>'


class WebhooksContext(WebhooksCollection):
    _endpoint = 'webhooks/{}'

    def __init__(self, token, client):
        super(WebhooksContext, self).__init__(client)
        self.token = token
        self.collections = Collection(client, WebhookPingModel)

    def ping(self, params=None):
        return self.collections.create(endpoint=self._endpoint.format(self.token)+'/ping', data = {}, query_params=params)

    def resend(self, event_type, event_token, params=None):
        return self.client.post(
            endpoint=self._endpoint.format(self.token) + '/{}/{}'.format(event_type, event_token),
            query_params=params)[0]
