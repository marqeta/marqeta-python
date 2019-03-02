from marqeta.errors import MarqetaError
from marqeta.resources.users import UsersCollection
import requests,json


headers = {'content-type': 'application/json',
            'User-Agent': '"marqeta-python/{} (Python {})".format(__version__)'}

class Client(object):

    def __init__(self, base_url=None, application_token=None, access_token=None):
        self.base_url = base_url
        self.application_token = application_token
        self.access_token = access_token
        objects = self._objects_container()
        self.users = objects['users']()

    def get(self, endpoint, query_params=None):
        response = requests.get(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                headers= headers,
                                params=query_params)
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return response.json(), response.status_code

    def put(self, endpoint, data):
        response = requests.put(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                headers=headers,
                                data=json.dumps(data))
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return response.json(), response.status_code

    def post(self, endpoint, data=None, query_params=None):
        response = requests.post(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                 headers=headers,
                                 params=query_params,
                                 data=json.dumps(data))
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return response.json(), response.status_code

    def delete(self, endpoint):
        response = requests.delete(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                   headers= headers)
        if response.status_code >= 400:
            response = response.json()
            raise MarqetaError(response['error_code'], response['error_message'])
        return (
            response.json(), response.status_code)

    def _objects_container(self):
        """
        Call subclasses via function to allow passing parent namespace to subclasses.

        Returns the dict with objects references.
        """
        _parent_class = self

        class UsersWrapper(UsersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        return {'users': UsersWrapper}