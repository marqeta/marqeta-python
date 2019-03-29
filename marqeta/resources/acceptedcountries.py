#!/usr/bin/env python3

from marqeta.resources.collection import Collection
from marqeta.response_models.accepted_countries_model import AcceptedCountriesModel


class AcceptedCountriesCollection(object):
    '''
    Marqeta API 'acceptedcountries' endpoint list, create, find and update operations
    '''
    _endpoint = 'acceptedcountries'

    def __init__(self, client):
        '''
        Creates a client collection object
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, AcceptedCountriesModel)

    def page(self, params=None):
        '''
        Provides the requested page for acceptedcountries
        :param params: query parameters
        :return: requested page with AcceptedCountriesModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: AcceptedCountriesModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the acceptedcountries
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of AcceptedCountriesModel object
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an acceptedcountries object
        :param data: data required for creation
        :param params: query parameters
        :return: AcceptedCountriesModel object of the created country
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds the existing country
        :param token: acceptedcountries token to find
        :param params: query parameters
        :return: AcceptedCountriesModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates the existing country data
        :param token: acceptedcountries token to update
        :param data: data to be updated
        :return:  AcceptedCountriesModel object of the updated  country
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.acceptedcountries.AcceptedCountriesCollection>'
