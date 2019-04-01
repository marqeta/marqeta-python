#!/usr/bin/env python3

'''BUSINESSES RESOURCE WITH CRU PARAMETERS'''

from marqeta.resources.collection import Collection
from marqeta.response_models.business_card_holder_model import BusinessCardHolderModel
from marqeta.response_models.business_card_holder_response import BusinessCardHolderResponse
from marqeta.response_models.business_card_holder_update_model import BusinessCardHolderUpdateModel
from marqeta.response_models.card_holder_model import CardHolderModel
from marqeta.response_models.cardholder_note_response_model import CardholderNoteResponseModel
from marqeta.response_models.business_transition_response import BusinessTransitionResponse
from marqeta.response_models.ssn_response_model import SsnResponseModel


class BusinessesCollection(object):
    '''
    Marqeta API 'businesses' endpoint list, create, find and update operations
    '''
    _endpoint = 'businesses'

    def __init__(self, client):
        '''
        Creates a client collection objects for different responses
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, BusinessCardHolderModel)
        self.collections_business = Collection(self.client,
                                               BusinessCardHolderResponse)
        self.collections_update = Collection(self.client,
                                             BusinessCardHolderUpdateModel)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: business token
        :return: BusinessContext object
        '''
        return BusinessContext(token, self.client)

    def page(self, count=5, start_index=0):
        '''
        Provides the requested page for businesses
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with BusinessCardHolderModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index)

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
        return self.collections.list(endpoint=self._endpoint, query_params=params,
                                     limit=limit)

    def create(self, data={}):
        '''
        Creates an businesses object
        :param data: data required for creation
        :return: BusinessCardHolderResponse object
        '''
        return self.collections_business.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific businesses object
        :param token: businesses token
        :param params: query parameters
        :return: BusinessCardHolderResponse object
        '''
        return self.collections_business.find(endpoint=self._endpoint + '/{}'.
                                              format(token), query_params=params)

    def save(self, token, data):
        '''
        Updates an businesses object
        :param token: businesses token
        :param data: data to be updated
        :return: BusinessCardHolderUpdateModel object
        '''
        return self.collections_update.save(data, endpoint=self._endpoint + '/{}'.
                                            format(token))

    def look_up(self, data, params=None):
        '''
        Lists all the business which matches the data fields
        :param data: data to look for
        :param params: query parameters
        :return: List of BusinessCardHolderModel object
        '''
        response = self.client.post(self._endpoint + '/lookup', data, query_params=params)[0]
        return BusinessCardHolderModel(response['data'])

    def __repr__(self):
        return '<Marqeta.resources.businesses.BusinessesCollection>'


class BusinessContext(BusinessesCollection):
    ''' class to specify sub endpoints for business '''

    def __init__(self, token, client):
        super(BusinessContext, self).__init__(client)
        self.token = token
        self.children = self.Children(self.token, Collection(client, CardHolderModel))
        self.notes = self.Notes(self.token, client, Collection(client,
                                                               CardholderNoteResponseModel))
        self.transitions = self.Transitions(self.token, Collection(client,
                                                                   BusinessTransitionResponse))

    def ssn(self, full_ssn=False):
        '''
        Provides SSN details
        :param full_ssn: set to True or False based on requirement
        :return: SsnResponseModel object
        '''
        response = self.client.get('businesses/{}/ssn'.format(self.token),
                                   query_params={'full_name': full_ssn})[0]
        return SsnResponseModel(response)

    class Children(object):
        '''
        Lists the children for parent business
        Returns CardHolderModel object
        '''

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0):
            return self.collection.page(count=count, start_index=start_index,
                                        endpoint='businesses/{}/children'.format(self.token))

        def stream(self, params=None):
            return self.collection.stream(query_params=params,
                                          endpoint='businesses/{}/children'.format(self.token))

        def list(self, params=None, limit=None):
            return self.collection.list(query_params=params,
                                        endpoint='businesses/{}/children'.format(self.token),
                                        limit=limit)

        def __repr__(self):
            return '<Marqeta.resources.businesses.BusinessContext.Children>'

    class Notes(object):
        '''
        Lists, Creates and Updates the notes for business
        Returns CardholderNoteResponseModel object
        '''
        _endpoint = 'businesses/{}/notes'

        def __init__(self, token, client, collection):
            self.token = token
            self.collection = collection
            self.client = client

        def page(self, count=5, start_index=0):
            return self.collection.page(endpoint=self._endpoint.format(self.token),
                                        count=count, start_index=start_index)

        def stream(self, params=None):
            return self.collection.stream(endpoint=self._endpoint.format(self.token),
                                          query_params=params)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint.format(self.token),
                                        query_params=params,
                                        limit=limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint.format(self.token))

        def save(self, notes_token, data):
            return self.collection.save(data,
                                        endpoint=self._endpoint.format(self.token) + '/{}'.
                                        format(notes_token))

        def __repr__(self):
            return '<Marqeta.resources.businesses.BusinessContext.Notes>'

    class Transitions(object):
        '''
        Lists, Creates and Finds the notes for business
        Returns BusinessTransitionResponse object
        '''
        _endpoint = 'businesstransitions'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0):
            return self.collection.page(count=count, start_index=start_index,
                                        endpoint=self._endpoint + '/business/{}'.format(self.token))

        def stream(self, params=None, limit=None):
            return self.collection.stream(query_params=params,
                                          endpoint=self._endpoint + '/business/{}'.format(self.token),
                                          limit=limit)

        def list(self, params=None, limit=None):
            return self.collection.list(query_params=params,
                                        endpoint=self._endpoint + '/business/{}'.format(self.token),
                                        limit=limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                endpoint=self._endpoint + '/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.businesses.BusinessContext.Transitions>'

    def __repr__(self):
        return '<Marqeta.resources.businesses.BusinessContext>'
