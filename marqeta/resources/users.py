#!/usr/bin/env python
"""USER RESOURCE WITH CRUD PARAMETERS"""
from marqeta.resources.users_resources import UserResource, NotesResources, TransitionsResources
from marqeta.resources.collections import Collections


class UsersCollection(object):

    """ place holder for the parent class """
    __user = None

    def __init__(self, client):
        self.client = client
        self.collections = Collections(self.client)

    def __call__(self, token):
        _parent_class = self
        return UserContext(token, self.client, _parent_class)
    ''' Iterates through users 
        returns user object one at a time'''
    def stream(self, endpoint='users', limit=float('inf'), resource=UserResource, **kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        return self.collections.stream(endpoint=endpoint, resource=resource, limit=limit, query_params=query_params)

    ''' Lists all the users Returns list of all user object '''
    def list(self, endpoint='users', resource=UserResource, limit=float('inf'), **kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        return self.collections.list(endpoint=endpoint,resource=resource, limit=limit, query_params=query_params)

    ''' Create the user with the specified data
            Returns the UserResource object which has created user information'''
    def create(self, data, resource=UserResource, endpoint='users'):
        return self.collections.create(endpoint=endpoint, resource=resource, data=data)
    ''' fields takes the list of fields delimited by ',' as a string'''

    ''' Finds the user information for the requested token
            Returns the UserResource object which has user information'''
    def find(self, token, endpoint=None, resource=UserResource, fields=None):
        return self.collections.find(token,endpoint=endpoint,resource=resource,fields=fields)

    ''' Update the user information for the requested token  with the data
                Returns the UserResource object which has updated user information'''
    def save(self, token, data, endpoint=None, resource=UserResource,):
        return self.collections.save(token, data, endpoint=endpoint,resource=resource)

    ''' Looks for the user information based on the specified data 
        Returns UserResource object of list of the matched users for the data '''
    def look_up(self, data, endpoint='users/lookup', resource=UserResource, **kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        response = self.client.post(endpoint, data, query_params=query_params)[0]
        return [resource(response['data'][val]) for val in range(response['count'])]


class UserContext(UsersCollection):

    def __init__(self, token, client, users_object):
        super(UserContext, self).__init__(client)
        self.token = token
        self.users_object = users_object
        self.children = self.Children(self.token, self.users_object)
        self.notes = self.Notes(self.token, self.users_object)
        self.transitions = self.Transitions(self.token, self.users_object)

    ''' for 'client.users({token).ssn()' -- user can specify to get full ssn '''

    def ssn(self, full_ssn=False):

        return self.client.get('users/{}/ssn'.format(self.token), query_params = {'full_name': full_ssn})[0]['ssn']

    class Children(object):

        def __init__(self, token, user_object):
            self.token = token
            self.users_object = user_object

        def list(self):
            return self.users_object.list(sort_by='-lastModifiedTime',
                                          endpoint='users/{}/children'.format(self.token))

    class Notes(object):

        def __init__(self, token, user_object):
            self.token = token
            self.users_object = user_object

        def list(self):
            return self.users_object.list(sort_by='-lastModifiedTime', resource=NotesResources,
                                          endpoint='users/{}/notes'.format(self.token))

        def create(self, data):
            return self.users_object.create(data, resource=NotesResources,
                                            endpoint='users/{}/notes'.format(self.token))

        def save(self, notes_token, data):
            return self.users_object.save(self.token, data, resource=NotesResources,
                                          endpoint='users/{}/notes/{}'.
                                          format(self.token, notes_token))

    class Transitions(object):

        def __init__(self, token, user_object):
            self.token = token
            self.users_object = user_object

        def list(self):
            return self.users_object.list(sort_by='-id', resource=TransitionsResources,
                                          endpoint='usertransitions/user/{}'.format(self.token))

        def create(self, data):
            return self.users_object.create(data, resource=TransitionsResources,
                                            endpoint='usertransitions')

        def find(self, transition_token):
            return self.users_object.find(self.token, resource=TransitionsResources,
                                          endpoint='usertransitions/{}'.format(transition_token))
