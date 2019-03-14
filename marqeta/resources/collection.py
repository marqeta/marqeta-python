#!/usr/bin/env python3
""" COLLECTION OF GENERIC CRU PARAMETERS """


class Collection(object):

    def __init__(self, client, resource):
        self.client = client
        self.resource = resource

    def _page(self, **kwargs):
        ''' sort_by can be specified in ascending or descending order "-" '''
        return self.client.get(kwargs['endpoint'], query_params=kwargs['query_params'])[0]

    ''' stream is a generator function iterates through endpoint contents
        Return : endpoint object, limit is the number of pages to fetch  '''
    def stream(self, endpoint=None,query_params=None):
        params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0}
        if query_params is not None:
            params.update(query_params)
        while True:
            response = self._page(endpoint=endpoint, query_params= params)
            if response['is_more'] is False:
                for count in range(response['count']):
                    yield (self.resource(response["data"][count]))
                break
            for count in range(response['count']):
                yield (self.resource(response["data"][count]))
            params['start_index'] = params['start_index'] + params['count']

    '''  Returns list of all endpoint object '''
    def list(self, endpoint=None, query_params=None, limit =float('inf')):
        list_of_user_object = []
        for count in self.stream(endpoint=endpoint, query_params=query_params):
            list_of_user_object.append(count)
            if len(list_of_user_object) == limit:
                break
        return list_of_user_object

    ''' Create the resource with the specified data
        Returns the Resource object '''

    def create(self, data, endpoint=None, query_params = None):
        response = self.client.post(endpoint, data, query_params)[0]
        return self.resource(response)

    ''' Finds the Resource information for the requested token
        Returns the Resource object '''

    def find(self, endpoint=None, query_params=None):
        response = self.client.get(endpoint, query_params=query_params)[0]
        return self.resource(response)

    ''' Update the Resource information for the requested token  with the data
            Returns the Resource object'''
    def save(self, data, endpoint=None):
        response = self.client.put(endpoint, data)[0]
        return self.resource(response)

    def __repr__(self):
        return '<Marqeta.resources.collection.Collection>'

