"""DIRECTDEPOSITS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.deposit_deposit_response import DepositDepositResponse
from marqeta.response_models.direct_deposit_transition_response import (
    DirectDepositTransitionResponse,
)

from marqeta.response_models.deposit_account import DepositAccount


class DirectDepositsCollection(object):
    """
    Marqeta API 'directdeposits' endpoint list, create, find and update operations
    """

    _endpoint = "directdeposits"

    def __init__(self, client):
        """
        Creates a client collection objects for different responses
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, DepositDepositResponse)

        self.accounts = Accounts(Collection(self.client, DepositAccount))

    def __call__(self, token):
        """
        Special case call made with token
        :param token: directdeposits token
        :return: DirectDepositsContext object
        """
        return DirectDepositsContext(token, self.client)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for directdeposits
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with DepositDepositResponse object for the requested
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
        :return: DepositDepositResponse object
        """
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        """
        List all the directdeposits
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of DepositDepositResponse object:
        """
        return self.collections.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def find(self, token, params=None):
        """
        Finds a specific directdeposits object
        :param token: directdeposits token
        :param params: query parameters
        :return: DepositDepositResponse object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def __repr__(self):
        return "<Marqeta.resources.directdeposits.DirectDepositsCollection>"


class Accounts(object):
    """Class for find and updating the directdeposit account"""

    _endpoint = "directdeposits/accounts"

    def __init__(self, collection):
        self.collections = collection

    def find(self, token, params=None):
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def __repr__(self):
        return "<Marqeta.resources.directdeposits.Accounts>"


class DirectDepositsContext(DirectDepositsCollection):
    """class to specify sub endpoints for directdeposits"""

    def __init__(self, token, client):

        super(DirectDepositsContext, self).__init__(client)

        self.token = token
        self.transitions = self.Transitions(
            self.token, Collection(client, DirectDepositTransitionResponse)
        )

    class Transitions(object):
        """
        Lists, Creates and Finds the notes for directdeposits
        Returns DirectDepositTransitionResponse object
        """

        _endpoint = "directdeposits/transitions"

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

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
            query_params = {"sort_by": "-id", "count": 5, "start_index": 0}
            if params is not None:
                query_params.update(params)
            return self.collection.list(
                endpoint=self._endpoint, query_params=query_params, limit=limit
            )

        def create(self, data, params=None):
            return self.collection.create(
                endpoint=self._endpoint, query_params=params, data=data
            )

        def find(self, token, params=None):
            return self.collection.find(
                endpoint=self._endpoint + "/{}".format(token), query_params=params
            )

        def __repr__(self):
            return (
                "<Marqeta.resources.directdeposits.DirectDepositsContext.Transitions>"
            )

    def __repr__(self):
        return "<Marqeta.resources.directdeposits.DirectDepositsContext>"
