from marqeta.resources.users_resources import UserResource, NotesResources, TransitionsResources

class Collections(object):

    def __init__(self, client):
        self.client = client

    def _page(self, **kwargs):
        ''' sort_by can be specified in ascending or descending order "-" '''
        return self.client.get(kwargs['endpoint'], query_params=kwargs['query_params'])[0]

    ''' stream is a generator function iterates through endpoint contents
        Return : endpoint object, limit is the number of pages to fetch  '''
    def stream(self, endpoint=None, limit= float('inf'), resource=None,**kwargs):
        query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        for key in kwargs:
            query_params[key] = kwargs[key]
        while True:
            response = self._page(endpoint=endpoint, query_params= query_params)
            if response['is_more'] is False or query_params['start_index'] == (limit * query_params['count'])-query_params['count']:
                break
            query_params['start_index'] = query_params['start_index'] + query_params['count']
            for user in range(response['count']):
                yield (resource(response["data"][user]))
        for user in range(response['count']):
            yield (resource(response["data"][user]))

    '''  Returns list of all endpoint object '''
    def list(self, endpoint=None, limit=float('inf'), resource=None, query_params=None):
        list_of_user_object = []
        while True:
            for user in self.stream(endpoint=endpoint,limit=limit, resource=resource, query_params=query_params):
                list_of_user_object.append(user)

            return list_of_user_object

    ''' Create the resource with the specified data
        Returns the Resource object '''

    def create(self, data, endpoint=None, resource=None, query_params = None):
        response = self.client.post(endpoint, data, query_params)[0]
        return resource(response)

    ''' Finds the Resource information for the requested token
        Returns the Resource object '''
    def find(self, token, endpoint=None, resource=None, fields = None):

        if endpoint is None:
            endpoint = 'users/{}'.format(token)
        else:
            endpoint = endpoint
        response = self.client.get(endpoint, query_params= {'fields':fields if fields is not None else {}})[0]
        return resource(response)

    ''' Update the Resource information for the requested token  with the data
            Returns the Resource object'''
    def save(self, token, data, endpoint=None, resource=None):
        if endpoint is None:
            endpoint = 'users/{}'.format(token)
        else: endpoint = endpoint
        response = self.client.put(endpoint, data)[0]
        return resource(response)

