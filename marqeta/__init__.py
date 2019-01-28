from __future__ import unicode_literals
from marqeta.errors import MarqetaError
from marqeta.version import __version__

import sys
import requests
import json

# Creating Client for HTTP headers

if sys.version_info < (3,):
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


class Client(object):

    def __init__(self,base_url = None, application_token = None, access_token = None):
        self.base_url = base_url
        self.application_token = application_token
        self.access_token = access_token

    # Get method to access the API information based on the endpoint, query parameters needs to be specified

    def get(self, endpoint, query_params = None):
        response = requests.get(url = self.base_url + endpoint,
                                auth = (self.application_token,self.access_token),
                                headers = {'content-type':'application/json',
                                           'User-Agent': '"marqeta-python/{} (Python {})".format(__version__)'},
                                params = query_params)
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return response.json(),response.status_code,

    # Put method to update the customer information to the specified end point.

    def put(self, endpoint, data):

        response = requests.put(url = self.base_url + endpoint,
                                auth = (self.application_token,self.access_token),
                                headers = {'content-type': 'application/json',
                                           'User-Agent': '"marqeta-python/{} (Python {})".format(__version__)'},
                                data = json.dumps(data))
        if response.status_code >= 400 :
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return response.json(), response.status_code,
    # Post method to create modules based on the specific information

    def post(self, endpoint, data = None):

        response = requests.post(url = self.base_url + endpoint,
                                 auth = (self.application_token,self.access_token),
                                 headers = {'content-type': 'application/json',
                                            'User-Agent': '"marqeta-python/{} (Python {})".format(__version__)'},
                                 data = json.dumps(data))
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return response.json(),response.status_code,

    # Delete method to delete the requested information

    def delete(self, endpoint):
        response = requests.delete(url = self.base_url + endpoint,
                                   auth = (self.application_token,self.access_token),
                                   headers = {'content-type': 'application/json',
                                              'User-Agent': '"marqeta-python/{} (Python {})".format(__version__)'})
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])

        return response.json(), response.status_code,






