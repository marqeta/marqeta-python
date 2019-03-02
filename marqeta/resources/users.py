#!/usr/bin/env python3
"""USER RESOURCE WITH CRU PARAMETERS"""
from marqeta.resources.users_resources import UserResource, NotesResources, TransitionsResources
from marqeta.resources.collection import Collection


class UsersCollection(object):

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, UserResource)
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}

    def __call__(self, token):
        return UserContext(token, self.client)
    ''' Iterates through users 
        returns user object one at a time'''
    def stream(self, endpoint='users', params = None):
        if params is not None :
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    ''' Lists all the users Returns list of all user object '''
    def list(self, endpoint='users', params=None, limit=float('inf')):
        if params is not None :
            self.query_params.update(params)
        return self.collections.list(endpoint=endpoint, query_params=self.query_params, limit=limit)

    ''' Create the user with the specified data
            Returns the UserResource object which has created user information'''
    def create(self, data={}, endpoint='users'):
        return self.collections.create(endpoint=endpoint, data=data)
    ''' fields takes the list of fields delimited by ',' as a string'''

    ''' Finds the user information for the requested token
            Returns the UserResource object which has user information
            fields is specified by as list of fields'''
    def find(self, token, endpoint='users', params=None):
        if params is not None :
            self.query_params.update(params)
        return self.collections.find(endpoint= endpoint+'/{}'.format(token),query_params=self.query_params)

    ''' Update the user information for the requested token  with the data
                Returns the UserResource object which has updated user information'''
    def save(self, token, data, endpoint='users'):
        return self.collections.save(data, endpoint=endpoint+'/{}'.format(token),)

    ''' Looks for the user information based on the specified data 
        Returns UserResource object of list of the matched users for the data '''
    def look_up(self, data, endpoint='users/lookup', params = None):
        if params is not None :
            self.query_params.update(params)
        response = self.client.post(endpoint, data, query_params=self.query_params)[0]
        return [UserResource(response['data'][val]) for val in range(response['count'])]


class UserContext(UsersCollection):

    def __init__(self, token, client):
        super(UserContext, self).__init__(client)
        self.token = token
        self.children = self.Children(self.token,Collection(client, UserResource))
        self.notes = self.Notes(self.token, Collection(client, NotesResources))
        self.transitions = self.Transitions(self.token, Collection(client, TransitionsResources))

    ''' for 'client.users({token).ssn()' -- user can specify to get full ssn '''

    def ssn(self, full_ssn=False):

        return self.client.get('users/{}/ssn'.format(self.token), query_params = {'full_name': full_ssn})[0]['ssn']

    class Children(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params = None,limit=float('inf')):
            query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
            if params is not None:
                query_params.update(params)
            return self.collection.list(endpoint='users/{}/children'.format(self.token),
                                        query_params=query_params,limit=limit)

    class Notes(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None,limit=float('inf')):
            query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
            if params is not None:
                query_params.update(params)
            return self.collection.list(endpoint='users/{}/notes'.format(self.token), query_params=query_params,
                                        limit =limit)

        def create(self, data):
            return self.collection.create(data, endpoint='users/{}/notes'.format(self.token))

        def save(self, notes_token, data):
            return self.collection.save(data,
                                        endpoint='users/{}/notes/{}'.format(self.token,
                                                                            notes_token))

    class Transitions(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, params= None,limit=float('inf')):
            query_params = {'sort_by': '-id', 'count': 5, 'start_index': 0}
            if params is not None:
                query_params.update(params)
            return self.collection.list(endpoint='usertransitions/user/{}'.format(self.token),query_params=query_params,
                                        limit = limit)

        def create(self, data):
            return self.collection.create(data,
                                          endpoint='usertransitions')

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint='usertransitions/{}'.format(transition_token))
