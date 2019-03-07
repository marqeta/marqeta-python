#!/usr/bin/env python3
"""CARD PRODUCT RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.card_product_response import CardProductResponse


class CardProductCollection(object):

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, CardProductResponse)
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    ''' Iterates through card products  
        returns card product object one at a time'''
    def stream(self, endpoint='cardproducts', params = None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    ''' Lists all the card products  Returns list of all card product object '''
    def list(self, endpoint='cardproducts', params=None, limit = float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=endpoint, query_params=self.query_params, limit=limit)

    ''' Create a card product with the specified data
            Returns the card product object which has created card product information'''
    def create(self, data = {}, endpoint='cardproducts'):
        return self.collections.create(endpoint=endpoint, data=data)

    ''' Finds the card product information for the requested token
            Returns the cardproduct object which has card product information '''
    def find(self, token, endpoint='cardproducts', params=None):
        return self.collections.find(endpoint= endpoint+'/{}'.format(token), query_params=params)

    ''' Update the card producy information for the requested token  with the data
                Returns the card product object which has updated user information'''
    def save(self, token, data, endpoint='cardproducts'):
        return self.collections.save(data, endpoint=endpoint+'/{}'.format(token),)

