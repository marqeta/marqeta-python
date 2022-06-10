"""REALTIMEFEEGROUPS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.real_time_fee_group import RealTimeFeeGroup


class RealTimeFeeGroupsCollection(object):
    """
    Marqeta API 'realtimefeegroups' endpoint list, create, find and update operations
    """

    _endpoint = "realtimefeegroups"

    def __init__(self, client):
        """
        Creates a client collection object
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, RealTimeFeeGroup)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for realtimefeegroups
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with RealTimeFeeGroup object for the requested
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
        :return: RealTimeFeeGroup object
        """
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        """
        List all the realtimefeegroups
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of RealTimeFeeGroup object
        """
        return self.collections.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def create(self, data, params=None):
        """
        Creates an realtimefeegroups object
        :param data: data required for creation
        :param params: query parameters
        :return: RealTimeFeeGroup object of the created realtimefeegroups
        """
        return self.collections.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        """
        Finds the existing realtimefeegroups
        :param token: realtimefeegroups token to find
        :param params: query parameters
        :return: RealTimeFeeGroup object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        """
        Updates the existing realtimefeegroups  data
        :param token: realtimefeegroups token to update
        :param data: data to be updated
        :return:  RealTimeFeeGroup object of the updated  realtimefeegroups
        """
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def __repr__(self):
        return "<Marqeta.resources.real_time_fee_groups.RealTimeFeeGroupsCollection>"
