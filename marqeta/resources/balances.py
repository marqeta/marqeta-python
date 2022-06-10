"""BALANCES/{TOKEN} RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.cardholder_balances import CardholderBalances


class BalancesCollection(object):
    """
    Marqeta API 'balances/{token}' endpoint list, create, find and update operations
    """

    _endpoint = "balances"

    def __init__(self, client):
        """
        Creates a client collection object
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, CardholderBalances)

    def page_msas_for_user_or_business(
        self, token, count=5, start_index=0, params=None
    ):
        """
        Provides the requested page for balances
        :param token: user or business token
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: CardholderBalances object
        """
        return self.collections.page(
            endpoint=self._endpoint + "/{}/msas".format(token),
            count=count,
            start_index=start_index,
            query_params=params,
        )

    def stream_msas_for_user_or_business(self, token, params=None):
        """
        Stream through the list of requested endpoint data field
        :param token: user or business token
        :param params: query parameters
        :return: CardholderBalances object
        """
        return self.collections.stream(
            endpoint=self._endpoint + "/{}/msas".format(token), query_params=params
        )

    def list_msas_for_user_or_business(self, token, params=None, limit=None):
        """
        Lists all the balances for specified token
        :param token: user or business token
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: list of CardholderBalances object
        """
        return self.collections.list(
            endpoint=self._endpoint + "/{}/msas".format(token),
            query_params=params,
            limit=limit,
        )

    def find_for_user_or_business(self, token, params=None):
        """
        Finds the user or business for balance token
        :param token: balance token
        :param params: uery parameters
        :return: ardholderBalances object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def __repr__(self):
        return "<Marqeta.resources.balances.BalancesCollection>"
