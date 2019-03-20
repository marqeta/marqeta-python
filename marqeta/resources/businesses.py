#!/usr/bin/env python3
"""BUSINESSES RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.business_card_holder_model import BusinessCardHolderModel
from marqeta.response_models.business_card_holder_response import BusinessCardHolderResponse
from marqeta.response_models.business_card_holder_update_model import BusinessCardHolderUpdateModel
from marqeta.response_models.card_holder_model import CardHolderModel
from marqeta.response_models.cardholder_note_response_model import CardholderNoteResponseModel
from marqeta.response_models.business_transition_response import BusinessTransitionResponse
from marqeta.response_models.ssn_response_model import SsnResponseModel


class BusinessesCollection(object):

    _endpoint = 'businesses'

    def __init__(self, client):
        self.client = client
        self.collections_business_model = Collection(self.client, BusinessCardHolderModel)
        self.collections_business_response_model = Collection(self.client, BusinessCardHolderResponse)
        self.collections_business_update_model = Collection(self.client, BusinessCardHolderUpdateModel)

    def __call__(self, token):
        return BusinessContext(token, self.client)
    ''' Iterates through businesses
        returns business object one at a time'''
    def stream(self, params=None):
        return self.collections_business_model.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the businesses Returns list of all business object '''
    def list(self, params=None, limit = None):
        return self.collections_business_model.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Creates a business user with the specified data
            Returns the BusinessCardHolderModel object which has created business user information'''
    def create(self, data = {}):
        return self.collections_business_model.create(endpoint=self._endpoint, data=data)

    ''' Finds the user information for the requested token
            Returns the UserResource object which has user information
            fields is specified by as list of fields'''
    def find(self, token, params=None):
        return self.collections_business_response_model.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    ''' Update the user information for the requested token  with the data
                Returns the UserResource object which has updated user information'''
    def save(self, token, data):
        return self.collections_business_update_model.save(data, endpoint=self._endpoint+'/{}'.format(token),)

    ''' Looks for the user information based on the specified data
        Returns UserResource object of list of the matched users for the data '''
    def look_up(self, data, params = None):
        query_params = {'count': 100, 'start_index': 0}
        if params is not None:
            query_params.update(params)
        look_up_data = []
        while True:
            response = self.client.post(self._endpoint + '/lookup', data, query_params=query_params)[0]
            if response['is_more'] is False:
                for val in range(response['count']):
                    look_up_data.append(CardHolderModel(response['data'][val]))
                break
            for val in range(response['count']):
                look_up_data.append(CardHolderModel(response['data'][val]))
            query_params['start_index'] = query_params['start_index'] + query_params['count']
        return look_up_data

    def __repr__(self):
        return '<Marqeta.resources.businesses.BusinessesCollection>'

class BusinessContext(BusinessesCollection):

    def __init__(self, token, client):
        super(BusinessContext, self).__init__(client)
        self.token = token
        self.children = self.Children(self.token,Collection(client, CardHolderModel))
        self.notes = self.Notes(self.token,client, Collection(client, CardholderNoteResponseModel))
        self.transitions = self.Transitions(self.token, Collection(client, BusinessTransitionResponse))

    ''' for 'client.users({token).ssn()' -- user can specify to get full ssn '''

    def ssn(self, full_ssn=False):
        response = self.client.get('businesses/{}/ssn'.format(self.token), query_params = {'full_name': full_ssn})[0]
        return SsnResponseModel(response['ssn'])

    def __repr__(self):
        return '<Marqeta.resources.businesses.BusinessContext>'


    class Children(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None, limit = None):
            return self.collection.list(query_params=params,
                                        endpoint='businesses/{}/children'.format(self.token), limit = limit)

        def __repr__(self):
            return '<Marqeta.resources.businesses.Children>'

    class Notes(object):
        _endpoint = 'businesses/{}/notes'

        def __init__(self, token,client, collection):
            self.token = token
            self.collection = collection
            self.client = client

        def list(self,params= None, limit = None):
            return self.collection.list(endpoint=self._endpoint.format(self.token), query_params=params, limit = limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint.format(self.token))

        def save(self, notes_token, data):
            return self.collection.save(data,
                                        endpoint=self._endpoint.format(self.token)+'/{}'.format(notes_token))

        def __repr__(self):
            return '<Marqeta.resources.businesses.Notes>'

    class Transitions(object):

        _endpoint = 'businesstransitions'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None, limit = None):
            return self.collection.list(query_params=params,
                                        endpoint=self._endpoint+'/business/{}'.format(self.token),limit = limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint=self._endpoint+'/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.businesses.Transitions>'
