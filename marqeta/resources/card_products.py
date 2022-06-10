"""CARDPRODUCTS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.card_product_response import CardProductResponse


class CardProductsCollection(object):
    """
    Marqeta API 'cardproducts' endpoint list, create, find and update operations
    """

    _endpoint = "cardproducts"

    def __init__(self, client):
        """
        Creates a client collection object
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, CardProductResponse)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for cardproducts
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with CardProductResponse object for the requested
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
        :return: CardProductResponse object
        """
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=25):
        """
        List all the cardproducts
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of CardProductResponse object
        """
        return self.collections.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def create(self, data, params=None):
        """
        Creates an cardproducts object
        :param data: data required for creation
        :param params: query parameters
        :return: CardProductResponse object of the created cardproducts
        """
        return self.collections.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        """
        Finds the existing cardproducts
        :param token: cardproducts token to find
        :param params: query parameters
        :return: CardProductResponse object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        """
        Updates the existing cardproducts  data
        :param token: cardproducts token to update
        :param data: data to be updated
        :return:  CardProductResponse object of the updated  cardproducts
        """
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def __repr__(self):
        return "<Marqeta.resources.card_products.CardProductsCollection>"
