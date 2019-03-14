#!/usr/bin/env python3
"""CARD PRODUCT RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.card_product_response import CardProductResponse


class CardProductCollection(object):

    _endpoint = 'cardproducts'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CardProductResponse)

    ''' Iterates through card products  
        returns card product object one at a time'''
    def stream(self, params = None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the card products  Returns list of all card product object '''
    def list(self, params=None, limit = float('inf')):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a card product with the specified data
            Returns the card product object which has created card product information'''
    def create(self, data, params= None):
        return self.collections.create(endpoint=self._endpoint,query_params=params, data=data)

    ''' Finds the card product information for the requested token
            Returns the cardproduct object which has card product information '''
    def find(self, token, params=None):
        return self.collections.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    ''' Update the card producy information for the requested token  with the data
                Returns the card product object which has updated user information'''
    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint+'/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.cardproducts.CardProductCollection>'
