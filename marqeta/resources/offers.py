#!/usr/bin/env python3

'''OFFERS RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.offer_response_model import OfferResponseModel


class OffersCollection(object):
    '''
     Marqeta API 'offers' endpoint list, create, find and update operations
    '''
    _endpoint = 'offers'

    def __init__(self, client):
        '''
        Creates a client collection objects
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, OfferResponseModel)

    def page(self, count=5, start_index=0):
        '''
        Provides the requested page for offers
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with OfferResponseModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count,
                                     start_index=start_index)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: OfferResponseModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the offers
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of OfferResponseModel object:
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an offers object
        :param data: data required for creation
        :param params: query parameters
        :return: OfferResponseModel object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific offers object
        :param token: offers token
        :param params: query parameters
        :return: OfferResponseModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def save(self, token, data):
        '''
        Updates an offers object
        :param token: offers token
        :param data: data to be updated
        :return: OfferResponseModel object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.offers.OffersCollection>'
