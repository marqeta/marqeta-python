#!/usr/bin/env python3

'''BUSINESSES RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.webhook_response_model import WebhookResponseModel
from marqeta.response_models.webhook_ping_model import WebhookPingModel


class WebhooksCollection(object):
    '''
     Marqeta API 'businesses' endpoint list, create, find and update operations
    '''
    _endpoint = 'webhooks'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, WebhookResponseModel)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: business token
        :return: BusinessContext object
        '''
        return WebhooksContext(token, self.client)

    def page(self, count=5, start_index=0):
        '''
        Provides the requested page for businesses
         :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with BusinessCardHolderModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: BusinessCardHolderModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the businesses
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of BusinessCardHolderModel object
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an businesses object
        :param data: data required for creation
        :param params: query parameters
        :return: BusinessCardHolderResponse object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific businesses object
        :param token: businesses token
        :param params: query parameters
        :return: BusinessCardHolderResponse object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an businesses object
        :param token: businesses token
        :param data: data to be updated
        :return: BusinessCardHolderUpdateModel object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.webhooks.WebhooksCollection>'


class WebhooksContext(WebhooksCollection):
    ''' class to specify sub endpoints for business '''

    _endpoint = 'webhooks/{}'

    def __init__(self, token, client):
        super(WebhooksContext, self).__init__(client)
        self.token = token
        self.collections = Collection(client, WebhookPingModel)

    def ping(self, params=None):
        '''
        Pings a webhook
        :param params: query parameters
        :return: WebhookPingModel object
        '''
        return self.collections.create(endpoint=self._endpoint.format(self.token) + '/ping',
                                       data={}, query_params=params)

    def resend(self, event_type, event_token, params=None):
        '''
        Replay an event to a webhook
        :param event_type: event type code
        :param event_token: even token
        :param params: query parameters
        :return: WebhookPingModel model
        '''
        return self.client.post(endpoint=self._endpoint.format(self.token) + '/{}/{}'.
                                format(event_type, event_token), query_params=params)[0]

    def __repr__(self):
        return '<Marqeta.resources.webhooks.WebhooksContext>'
