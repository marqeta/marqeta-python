"""AUTHCONTROLS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.auth_control_response import AuthControlResponse
from marqeta.response_models.auth_control_exempt_mids_response import (
    AuthControlExemptMidsResponse,
)


class AuthControlsCollection(object):
    """
    Marqeta API 'authcontrols' endpoint list, create, find and update operations
    """

    _endpoint = "authcontrols"

    def __init__(self, client):
        """
        Creates a client collection objects for different responses
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, AuthControlResponse)

        self.exempt_mids = AuthcontrolsExemptmidsCollection(self.client)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for authcontrols
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with AuthControlResponse object for the requested
        page 'data'field
        """
        return self.collections.page(
            endpoint=self._endpoint,
            count=count,
            start_index=start_index,
            query_params=params,
        )

    def stream(self, params=None):
        """
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: AuthControlResponse object
        """
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        """
        List all the authcontrols
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of AuthControlResponse object:
        """
        return self.collections.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def create(self, data, params=None):
        """
        Creates an authcontrols object
        :param data: data required for creation
        :param params: query parameters
        :return: AuthControlResponse object
        """
        return self.collections.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        """
        Finds a specific authcontrols object
        :param token: authcontrols token
        :param params: query parameters
        :return: AuthControlResponse object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        """
        Updates an authcontrols object
        :param token: authcontrols token
        :param data: data to be updated
        :return: AuthControlResponse object
        """
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def __repr__(self):
        return "<Marqeta.resources.authcontrols.AuthControlsCollection>"


class AuthcontrolsExemptmidsCollection(object):

    """class to specify sub endpoints for authcontrols"""

    _endpoint = "authcontrols/exemptmids"

    def __init__(self, client):
        self.client = client
        self.collection = Collection(self.client, AuthControlExemptMidsResponse)

    def page(self, count=5, start_index=0, params=None):
        return self.collection.page(
            endpoint=self._endpoint,
            count=count,
            start_index=start_index,
            query_params=params,
        )

    def stream(self, params=None):
        return self.collection.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        return self.collection.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def create(self, data, params=None):
        return self.collection.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        return self.collection.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        return self.collection.save(data, endpoint=self._endpoint + "/{}".format(token))

    def __repr__(self):
        return "<Marqeta.resources.authcontrols_exemptmids.AuthcontrolsExemptmidsCollection>"
