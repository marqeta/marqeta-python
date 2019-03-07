#!/usr/bin/env python3
"""GPA Order RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.gpa_response import GpaResponse
from marqeta.response_models.gpa_returns import GpaReturns


class GpaCollection(object):

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, GpaResponse)
        self.unloads = Unloads(Collection(self.client, GpaReturns))

    ''' Create a gpa product with the specified data
            Returns the gpa product object which has created gpa  information'''
    def create(self, data = {}, endpoint='gpaorders'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, token, endpoint='gpaorders', params=None):
        return self.collections.find(endpoint= endpoint+'/{}'.format(token), query_params=params)


class Unloads(object):

    def __init__(self, collection):
        self.collections = collection
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    def stream(self, endpoint='gpaorders/unloads', params = None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=endpoint, query_params=self.query_params)

    def list(self, endpoint='gpaorders/unloads', params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=endpoint, query_params=self.query_params, limit=limit)

    def create(self, data = {}, endpoint='gpaorders/unloads'):
        return self.collections.create(endpoint=endpoint, data=data)

    def find(self, token, endpoint='gpaorders/unloads', params=None):
        return self.collections.find(endpoint= endpoint+'/{}'.format(token), query_params=params)
