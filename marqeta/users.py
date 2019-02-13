from marqeta.users_resources import UserResource,NotesResources,TransitionsResources
''' UserCollection class lists, creates, updates
and finds the user information '''


class UsersCollection(object):

    """ place holder for the parent class """
    __user = None

    def __init__(self,client):
        self.client = client

    def __call__(self,token):
        _parent_class = self
        return UsersContext(token, self.client,_parent_class)

    def _page(self,**kwargs):
        ''' sort_by can be specified in ascending or descending order "-" '''

        return self.client.get('{}?count={}&start_index={}&sort_by={}'.format(kwargs['endpoint'],kwargs['count'],
                                                                                  kwargs['start_index'],
                                                                                  kwargs['sort_by']))[0]

    ''' Lists all the users 
        Returns list of all user object '''
    def list(self, sort_by = '-lastModifiedTime', endpoint ='users', resource = UserResource):                 # sort_by=None):
        count = 5
        start_index = 0
        list_of_users =[]
        while True:
            response = self._page(endpoint = endpoint ,count= count, start_index = start_index, sort_by=sort_by)
            if response['is_more'] == False or start_index == 5:  # start_index is specified only for testing
                list_of_users += [(resource(response["data"][count])) for count in range(response['count'])]
                break
            start_index = start_index + count
            list_of_users += [resource(response["data"][count]) for count in range(response['count'])]
        return list_of_users

    ''' Create the user with the specified data
        Returns the UserResource object which has created user information'''
    def create(self, data, resource = UserResource, endpoint ='users' ):

        response = self.client.post(endpoint, data)[0]
        return resource(response)

    ''' Finds the user information for the requested token 
        Returns the UserResource object which has user information'''
    def find(self,token, endpoint = None, resource = UserResource):
        if endpoint == None:
            endpoint = 'users/{}'.format(token)
        else: endpoint = endpoint
        response = self.client.get('users/{}'.format(token))[0]
        return resource(response)

    ''' Update the user information for the requested token  with the data
            Returns the UserResource object which has updated user information'''
    def save(self,token, data, endpoint = None, resource = UserResource):
        if endpoint == None:
            endpoint = 'users/{}'.format(token)
        else: endpoint = endpoint
        response = self.client.put(endpoint,data)[0]
        return resource(response)


class UsersContext(UsersCollection):

    def __init__(self, token,client, users_object):
        super(UsersContext, self).__init__(client)
        self.token = token
        self.users_object = users_object
        self.children = self.Children(self.token, self.users_object)
        self.notes = self.Notes(self.token,self.users_object)
        self.transitions = self.Transitions(self.token,self.users_object)

    ''' for 'client.users({token).ssn()' -- user can specify to get full ssn '''
    def ssn(self,full_ssn = False):

        return self.client.get('users/{}/ssn?full_ssn={}'.format(self.token, full_ssn))[0]['ssn']

    class Children(object):

        def __init__(self, token, user_object):
            self.token = token
            self.users_object = user_object

        def list(self):
            return self.users_object.list(sort_by='-lastModifiedTime', endpoint='users/{}/children'.format(self.token))

    class Notes(object):

        def __init__(self, token, user_object):
            self.token = token
            self.users_object = user_object

        def list(self):
            return self.users_object.list(sort_by='-lastModifiedTime', endpoint='users/{}/notes'.format(self.token),
                                          resource = NotesResources)

        def create(self, data):
            return self.users_object.create(data, resource = NotesResources, endpoint = 'users/{}/notes'.format(self.token))

        def save(self,notes_token,data):
            return self.users_object.save(self.token, data, resource = NotesResources, endpoint= 'users/{}/notes/{}'.
                                          format(self.token,notes_token))

    class Transitions(object):

        def __init__(self, token, user_object):
            self.token = token
            self.users_object = user_object

        def list(self):
            return self.users_object.list(sort_by='-id', endpoint='usertransitions/user/{}'.format(self.token),
                                          resource=TransitionsResources)

        def create(self,data):
            return self.users_object.create(data, resource = TransitionsResources, endpoint = 'usertransitions')

        def find(self,transition_token):
            return self.users_object.find(self.token, resource=TransitionsResources, endpoint='usertransitions/{}'.
                                          format(transition_token))




