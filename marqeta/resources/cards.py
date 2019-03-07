#!/usr/bin/env python3
"""CARDS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.card_response import CardResponse
from marqeta.response_models.pan_response import PanResponse
from marqeta.response_models.card_transition_response import CardTransitionResponse



class CardsCollection(object):

    def __init__(self, client):
        self.client = client
        self.collections_card_response = Collection(self.client, CardResponse)
        self.collections_pan_response = Collection(self.client, PanResponse)
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    def __call__(self, token):
        return CardsContext(token, self.client)
    ''' Iterates through cards based on last_four number
        returns card object one at a time'''
    def stream(self, last_four, endpoint='cards', params = None):
        if params is not None:
            self.query_params.update(params)
        self.query_params['last_four'] = last_four
        return self.collections_card_response.stream(endpoint=endpoint, query_params=self.query_params)

    ''' Lists all the cards Returns list of all card object based on last_four number of card'''
    def list(self,last_four, endpoint='cards', params=None, limit = float('inf')):
        if params is not None:
            self.query_params.update(params)
        self.query_params['last_four'] = last_four
        return self.collections_card_response.list(endpoint=endpoint, query_params=self.query_params, limit=limit)

    ''' Lists all the cards Returns list of all card object based on user token '''
    def list_for_user(self,user_token, endpoint='cards', params=None, limit = float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections_card_response.list(endpoint=endpoint+"/user/{}".format(user_token), query_params=self.query_params, limit=limit)

    ''' Creates a card with the specified data
            Returns the card object which has created card information'''
    def create(self, data = {}, endpoint='cards'):
        return self.collections_card_response.create(endpoint=endpoint, data=data)

    ''' Finds the card information for the requested card token
            Returns the card object which has card information '''
    def find(self, card_token, endpoint='cards', params=None):
        return self.collections_card_response.find(endpoint= endpoint+'/{}'.format(card_token), query_params=params)

    ''' Finds the card number information for the requested card token
                Returns the card object which has card number '''
    def find_show_pan(self,card_token, endpoint='cards', params=None):
        return self.collections_card_response.find(endpoint= endpoint+'/{}/showpan'.format(card_token), query_params=params)

    ''' Finds the card information for the requested barcode
                Returns the card object which has card information '''
    def find_by_barcode(self,barcode, endpoint='cards', params=None):
        return self.collections_card_response.find(endpoint= endpoint+'/find_by_barcode/{}'.format(barcode), query_params=params)

    ''' Finds the card information for the requested card token
                Returns the card object which has card information '''
    def find_for_merchant(self,token, endpoint='cards', params=None):
        return self.collections_card_response.find(endpoint= endpoint+'/merchant/{}'.format(token), query_params=params)

    ''' Finds the card information for the requested card token
                Returns the card object which has card information '''
    def find_for_merchant_show_pan(self,token, endpoint='cards', params=None):
        return self.collections_card_response.find(endpoint= endpoint+'/merchant/{}/showpan'.format(token), query_params=params)

    ''' Finds the card information for the requested card token
                Returns the card object which has card information '''
    def create_for_merchant(self,token, endpoint='cards', params=None):
        return self.collections_card_response.create(endpoint= endpoint+'/merchant/{}'.format(token), query_params=params)

    ''' Finds the card information for the requested card token
                Returns the card object which has card information '''
    def tokens_for_pan(self,pan, endpoint='cards'):
        return self.collections_pan_response.create(endpoint= endpoint+'/getbypan', data=pan)

    ''' Update the card information for the requested token  with the data
                Returns the card object which has updated card information'''
    def save(self, token, data, endpoint='cards'):
        return self.collections_card_response.save(data, endpoint=endpoint+'/{}'.format(token),)



class CardsContext(CardsCollection):

    def __init__(self, token, client):
        super(CardsContext, self).__init__(client)
        self.token = token
        self.transitions = self.Transitions(self.token, Collection(client, CardTransitionResponse))

    ''' list, create and find operations for cards transition'''
    class Transitions(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, **kwargs):
            query_params = {'sort_by': '-id', 'count': 5, 'start_index': 0}
            for key in kwargs:
                query_params[key] = kwargs[key]
            return self.collection.list(query_params=query_params,
                                        endpoint='cardtransitions/card/{}'.format(self.token))

        def create(self, data):
            return self.collection.create(data,
                                          endpoint='cardtransitions')

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint='cardtransitions/{}'.format(transition_token))
