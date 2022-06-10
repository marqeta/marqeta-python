"""FEES RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.fee import Fee


class FeesCollection(object):
    """
    Marqeta API 'fees' endpoint list, create, find and update operations
    """

    _endpoint = "fees"

    def __init__(self, client):
        """
        Creates a client collection object
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, Fee)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for fees
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with Fee object for the requested
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
        :return: Fee object
        """
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        """
        List all the fees
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of Fee object
        """
        return self.collections.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def create(self, data, params=None):
        """
        Creates an fees object
        :param data: data required for creation
        :param params: query parameters
        :return: Fee object of the created fees
        """
        return self.collections.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        """
        Finds the existing fees
        :param token: fees token to find
        :param params: query parameters
        :return: Fee object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        """
        Updates the existing fees  data
        :param token: fees token to update
        :param data: data to be updated
        :return:  Fee object of the updated  fees
        """
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def __repr__(self):
        return "<Marqeta.resources.fees.FeesCollection>"
