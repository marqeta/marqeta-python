#!/usr/bin/env python3
"""USER RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.card_holder_model import CardHolderModel
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse
from marqeta.response_models.cardholder_note_response_model import CardholderNoteResponseModel
from marqeta.response_models.user_transition_response_model import UserTransitionResponse
from marqeta.response_models.ssn_response_model import SsnResponseModel


class UsersCollection(object):

    _endpoint = 'users'

    def __init__(self, client):
        self.client = client
        self.collections_cardmodel = Collection(self.client, CardHolderModel)
        self.collections_usermodel = Collection(self.client, UserCardHolderResponse)

    def __call__(self, token):
        return UserContext(token, self.client)
    ''' Iterates through users
        returns user object one at a time'''
    def stream(self, params=None):
        return self.collections_cardmodel.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the users Returns list of all user object '''
    def list(self, params=None, limit = float('inf')):
        return self.collections_cardmodel.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Creates a user with the specified data
            Returns the UserResource object which has created user information'''
    def create(self, data = {}):
        return self.collections_usermodel.create(endpoint=self._endpoint, data=data)
    ''' fields takes the list of fields delimited by ',' as a string'''

    ''' Finds the user information for the requested token
            Returns the UserResource object which has user information'''
    def find(self, token, params=None):
        return self.collections_usermodel.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    ''' Update the user information for the requested token  with the data
                Returns the UserResource object which has updated user information'''
    def save(self, token, data):
        return self.collections_cardmodel.save(data, endpoint=self._endpoint+'/{}'.format(token),)

    ''' Looks for the user information based on the specified data
        Returns UserResource object of list of the matched users for the data '''
    def look_up(self, data, params = None):
        response = self.client.post(self._endpoint+'/lookup', data, query_params=params)[0]
        return [CardHolderModel(response['data'][val]) for val in range(response['count'])]

    def __repr__(self):
        return '<Marqeta.resources.users.UsersCollection>'


class UserContext(UsersCollection):

    def __init__(self, token, client):
        super(UserContext, self).__init__(client)
        self.token = token
        self.children = self.Children(self.token,Collection(client, CardHolderModel))
        self.notes = self.Notes(self.token, Collection(client, CardholderNoteResponseModel))
        self.transitions = self.Transitions(self.token, Collection(client, UserTransitionResponse))

    ''' for 'client.users({token).ssn()' -- user can specify to get full ssn '''

    def ssn(self, full_ssn=False):
        response = self.client.get('users/{}/ssn'.format(self.token), query_params = {'full_name': full_ssn})[0]
        return SsnResponseModel(response['ssn'])

    def __repr__(self):
        return '<Marqeta.resources.users.UserContext>'

    class Children(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params = None,limit=float('inf')):
            return self.collection.list(endpoint='users/{}/children'.format(self.token),
                                        query_params=params,limit=limit)

    class Notes(object):

        _endpoint = 'users/{}/notes'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None,limit=float('inf')):
            return self.collection.list(endpoint=self._endpoint.format(self.token), query_params=params,
                                        limit =limit)

        def create(self, data):
            return self.collection.create(data, endpoint=self._endpoint.format(self.token))

        def save(self, notes_token, data):
            return self.collection.save(data,
                                        endpoint=self._endpoint.format(self.token)+'/{}'.format(notes_token))

        def __repr__(self):
            return '<Marqeta.resources.users.Notes>'

    class Transitions(object):

        _endpoint = 'usertransitions'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None,limit=float('inf')):
            query_params = {'sort_by': '-id', 'count': 5, 'start_index': 0}
            if params is not None:
                query_params.update(params)
            return self.collection.list(endpoint=self._endpoint+'/user/{}'.format(self.token),query_params=query_params,
                                        limit = limit)

        def create(self, data):
            return self.collection.create(data,
                                          endpoint=self._endpoint)

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint=self._endpoint+'/{}'.format(transition_token))

        def __repr__(self):
            return '<Marqeta.resources.users.Transitions>'
