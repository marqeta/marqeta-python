from __future__ import absolute_import, division, print_function

from marqeta.errors import MarqetaError
from marqeta.resources.users import UsersCollection
from marqeta.resources.cardproducts import CardProductCollection
from marqeta.resources.cards import CardsCollection
from marqeta.resources.gpa_order import GpaCollection
from marqeta.resources.funding_sources import FundingSourcesCollection
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
        self.card_products = objects['card_products']()
        self.cards = objects['cards']()
        self.funding_sources = objects['funding_sources']()
        self.gpa_orders = objects['gpa_orders']()


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

        class CardProductWrapper(CardProductCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class CardsWrapper(CardsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class GpaWrapper(GpaCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class FundingWrapper(FundingSourcesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        return {'users': UsersWrapper,
                'card_products': CardProductWrapper,
                'cards': CardsWrapper,
                'gpa_orders': GpaWrapper,
                'funding_sources': FundingWrapper
                }

