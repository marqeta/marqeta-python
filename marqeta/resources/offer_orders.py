"""OFFERORDERS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.offer_order_response import OfferOrderResponse


class OfferOrdersCollection(object):
    """
    Marqeta API 'offerorders' endpoint list, create, find and update operations
    """

    _endpoint = "offerorders"

    def __init__(self, client):
        """
        Creates a client collection object
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, OfferOrderResponse)

    def create(self, data, params=None):
        """
        Creates an offerorders object
        :param data: data required for creation
        :param params: query parameters
        :return: OfferOrderResponse object of the created offerorders
        """
        return self.collections.create(
            endpoint=self._endpoint, query_params=params, data=data
        )

    def find(self, token, params=None):
        """
        Finds the existing offerorders
        :param token: offerorders token to find
        :param params: query parameters
        :return: OfferOrderResponse object
        """
        return self.collections.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def __repr__(self):
        return "<Marqeta.resources.offer_orders.OfferOrdersCollection>"
