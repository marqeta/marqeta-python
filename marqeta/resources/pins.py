"""PINS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.control_token_response import ControlTokenResponse


class PinsCollection(object):
    """
    Marqeta API 'pins' endpoint list, create, find and update operations
    """

    _endpoint = "pins"

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, ControlTokenResponse)

    def new(self, data):
        """
        Creates an pins object
        :param data: data required for creation
        :return: ControlTokenResponse object
        """
        return self.collections.create(endpoint=self._endpoint, data=data)

    """ Lists all the offers  Returns list of all offers object """

    def create_control_token(self, data):
        """
        Updates an pins object
        :param data: data to be updated
        :return: ControlTokenResponse object
        """
        return self.collections.save(
            endpoint=self._endpoint + "/controltoken", data=data
        )

    def __repr__(self):
        return "<Marqeta.resources.pins.PinsCollection>"
