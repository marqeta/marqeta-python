#!/usr/bin/env python3
"""USER RESOURCE WITH CRU PARAMETERS"""
from marqeta.resources.users_resources import UserResource, NotesResources, TransitionsResources
from marqeta.resources.collection import Collection


class UsersCollection(object):

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, UserResource)

    def __call__(self, token):
        return UserContext(token, self.client)
    ''' Iterates through users 
        returns user object one at a time'''
    def stream(self, endpoint='users', limit=float('inf'), **kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        return self.collections.stream(endpoint=endpoint, limit=limit, query_params=query_params)

    ''' Lists all the users Returns list of all user object '''
    def list(self, endpoint='users', limit=float('inf'), **kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        print("list paramertes inside the users", query_params)
        return self.collections.list(endpoint=endpoint, limit=limit, query_params=query_params)

    ''' Create the user with the specified data
            Returns the UserResource object which has created user information'''
    def create(self, data, endpoint='users'):
        return self.collections.create(endpoint=endpoint, data=data)
    ''' fields takes the list of fields delimited by ',' as a string'''

    ''' Finds the user information for the requested token
            Returns the UserResource object which has user information
            fields is specified by as list of fields'''
    def find(self, token, endpoint='users', fields=None):
        return self.collections.find(endpoint= endpoint+'/{}'.format(token), fields=fields)

    ''' Update the user information for the requested token  with the data
                Returns the UserResource object which has updated user information'''
    def save(self, token, data, endpoint='users'):
        return self.collections.save(data, endpoint=endpoint+'/{}'.format(token),)

    ''' Looks for the user information based on the specified data 
        Returns UserResource object of list of the matched users for the data '''
    def look_up(self, data, endpoint='users/lookup', **kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        response = self.client.post(endpoint, data, query_params=query_params)[0]
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

        def list(self,**kwargs):
            query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
            for key in kwargs:
                query_params[key] = kwargs[key]
            return self.collection.list(query_params=query_params,
                                        endpoint='users/{}/children'.format(self.token))

    class Notes(object):

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def list(self, **kwargs):
            query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
            for key in kwargs:
                query_params[key] = kwargs[key]
            return self.collection.list(query_params=query_params,
                                        endpoint='users/{}/notes'.format(self.token))

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

        def list(self, **kwargs):
            query_params = {'sort_by': '-id', 'count': 5, 'start_index': 0}
            for key in kwargs:
                query_params[key] = kwargs[key]
            return self.collection.list(query_params=query_params,
                                        endpoint='usertransitions/user/{}'.format(self.token))

        def create(self, data):
            return self.collection.create(data,
                                          endpoint='usertransitions')

        def find(self, transition_token):
            return self.collection.find(
                                        endpoint='usertransitions/{}'.format(transition_token))
