#!/usr/bin/env python3

'''PUSHTOCARDS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.push_to_card_disbursement_response import PushToCardDisbursementResponse
from marqeta.response_models.push_to_card_response import PushToCardResponse


class PushToCardsCollection(object):
    '''
    Marqeta API 'pushtocards' endpoint list, create, find and update operations
    '''

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections_pushtocards = Collection(self.client, PushtocardsPaymentcardCollection)
        self.disburse = PushtocardsDisburseCollection(self.client)
        self.payment_card = PushtocardsPaymentcardCollection(self.client)


class PushtocardsDisburseCollection(object):
    _endpoint = 'pushtocards/disburse'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections_disburse = Collection(self.client, PushToCardDisbursementResponse)

    def page(self, count=5, start_index=0, params=None):
        '''
         Provides the requested page for pushtocards disburse
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with PushToCardDisbursementResponse object for the requested
        page 'data'field
        '''
        return self.collections_disburse.page(endpoint=self._endpoint, count=count,
                                              start_index=start_index, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: PushToCardDisbursementResponse object
        '''
        return self.collections_disburse.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the  pushtocards disburse
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of PushToCardDisbursementResponse object
        '''
        return self.collections_disburse.list(endpoint=self._endpoint, query_params=params,
                                              limit=limit)

    def create(self, data, params=None):
        '''
        Creates an  pushtocards disburse object
        :param data: data required for creation
        :param params: query parameters
        :return: PushToCardDisbursementResponse object
        '''
        return self.collections_disburse.create(endpoint=self._endpoint, query_params=params,
                                                data=data)

    def find(self, token, params=None):
        '''
        Finds a specific  pushtocards disburse object
        :param token:  pushtocards disburse token
        :param params: query parameters
        :return: PushToCardDisbursementResponse object
        '''
        return self.collections_disburse.find(endpoint=self._endpoint + '/{}'.format(token),
                                              query_params=params)

    def save(self, token, data):
        '''
        Updates an  pushtocards disburse object
        :param token:  pushtocards disburse token
        :param data: data to be updated
        :return: PushToCardDisbursementResponse object
        '''
        return self.collections_disburse.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.pushtocards.PushtocardsDisburseCollection>'


class PushtocardsPaymentcardCollection(object):
    '''
    Class for pushtocode for paymentcard
    Lists, Create and Find pushtocode for paymentcard
    Returns PushToCardResponse object
    '''

    _endpoint = 'pushtocards/paymentcard'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, PushToCardResponse)

    def page_for_user(self, token, params=None,count=5, start_index=0):
        query_params = {'user_token': token}
        if params is not None:
            query_params.update(params)
        return self.collections.page(endpoint=self._endpoint, query_params=query_params,
                                     count=count, start_index=start_index)

    def stream_for_user(self, token, params=None):
        query_params = {'user_token': token}
        if params is not None:
            query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint, query_params=query_params)

    def list_for_user(self, token, params=None, limit=None):
        query_params = {'user_token': token}
        if params is not None:
            query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=query_params,
                                     limit=limit)

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.pushtocards.PushtocardsPaymentcardCollection>'
