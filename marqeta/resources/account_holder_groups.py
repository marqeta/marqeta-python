"""ACCOUNTHOLDERGROUPS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.account_holder_group_response import (
    AccountHolderGroupResponse,
)


class AccountHolderGroupsCollection(object):
    """
    Marqeta API 'accountholdergroups' endpoint list, create, find and update operations
    """

    _endpoint = "accountholdergroups"

    def __init__(self, client):
        """
        Creates a client collection object
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, AccountHolderGroupResponse)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for accountholdergroups
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with AccountHolderGroupResponse object for the requested
        page 'data'field
        """
        query_params = {"count": 10}
        if params is not None:
            query_params.update(params)
        return self.collections.page(
            endpoint=self._endpoint,
            count=count,
            start_index=start_index,
            query_params=query_params,
        )

    def stream(self, params=None):
        """
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: AccountHolderGroupResponse object
        """
        query_params = {"count": 10}
        if params is not None:
            query_params.update(params)
        return self.collections.stream(
            endpoint=self._endpoint, query_params=query_params
        )

    def list(self, params=None, limit=None):
        """
        List all the accountholdergroups
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of AccountHolderGroupResponse object
        """
        query_params = {"count": 10}
        if params is not None:
            query_params.update(params)
        return self.collections.list(
            endpoint=self._endpoint, query_params=query_params, limit=limit
        )

    def create(self, data, params=None):
        """
        Creates an accountholdergroups object
        :param data: data required for creation
        :param params: query parameters
        :return: AccountHolderGroupResponse object of the created accountholdergroups
        """
        return self.collections.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        """
        Finds the existing accountholdergroups
        :param token: accountholdergroups token to find
        :param params: query parameters
        :return: AccountHolderGroupResponse object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        """
        Updates the existing accountholdergroups  data
        :param token: accountholdergroups token to update
        :param data: data to be updated
        :return:  AccountHolderGroupResponse object of the updated  accountholdergroups
        """
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def __repr__(self):
        return "<Marqeta.resources.account_holder_groups.AccountHolderGroupsCollection>"
