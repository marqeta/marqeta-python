"""USERS RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse
from marqeta.response_models.card_holder_model import CardHolderModel
from marqeta.response_models.user_transition_response import UserTransitionResponse
from marqeta.response_models.cardholder_note_response_model import (
    CardholderNoteResponseModel,
)
from marqeta.response_models.ssn_response_model import SsnResponseModel


class UsersCollection(object):
    """
    Marqeta API 'users' endpoint list, create, find and update operations
    """

    _endpoint = "users"

    def __init__(self, client):
        """
        Creates a client collection objects for different responses
        :param client: client object
        """
        self.client = client
        self.collections = Collection(self.client, CardHolderModel)
        self.collections_usermodel = Collection(self.client, UserCardHolderResponse)

    def __call__(self, token):
        """
        Special case call made with token
        :param token: users token
        :return: UsersContext object
        """
        return UsersContext(token, self.client)

    def page(self, count=5, start_index=0, params=None):
        """
        Provides the requested page for users
        :param count: data to be displayed per page
        :param start_index: start_index
        :param params: query parameters
        :return: requested page with CardHolderModel object for the requested
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
        :return: CardHolderModel object
        """
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=1000):
        """
        List all the users
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of CardHolderModel object
        """
        return self.collections.list(
            endpoint=self._endpoint, query_params=params, limit=limit
        )

    def create(self, data={}):
        """
        Creates an users object
        :param data: data required for creation
        :return:UserCardHolderResponse object
        """
        return self.collections_usermodel.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        """
        Finds a specific users object
        :param token: users token
        :param params: query parameters
        :return:UserCardHolderResponse object
        """
        return self.collections_usermodel.find(
            endpoint=self._endpoint + "/{}".format(token), query_params=params
        )

    def save(self, token, data):
        """
        Updates an users object
        :param token: users token
        :param data: data to be updated
        :return: CardHolderModel object
        """
        return self.collections.save(
            data, endpoint=self._endpoint + "/{}".format(token)
        )

    def look_up(self, data, params=None, limit=1000):
        """
        Returns all the users which matches the data fields
        :param data: data to look for
        :param params: query parameters
        :return:  object
        """
        if not data:
            return self.collections.list(
                endpoint=self._endpoint, query_params=params, limit=limit
            )
        else:
            query_params = {"count": 5, "start_index": 0}
            if params is not None:
                query_params.update(params)
            look_up_data = []
            while True:
                response = self.client.post(
                    self._endpoint + "/lookup", data, query_params=query_params
                )[0]
                if response["is_more"] is False:
                    for val in range(response["count"]):
                        look_up_data.append(CardHolderModel(response["data"][val]))
                    break
                for val in range(response["count"]):
                    look_up_data.append(CardHolderModel(response["data"][val]))
                query_params["start_index"] = (
                    query_params["start_index"] + query_params["count"]
                )
            return look_up_data

    def __repr__(self):
        return "<Marqeta.resources.users.UsersCollection>"


class UsersContext(UsersCollection):
    """class to specify sub endpoints for users"""

    def __init__(self, token, client):
        super(UsersContext, self).__init__(client)
        self.token = token
        self.children = self.Children(self.token, Collection(client, CardHolderModel))
        self.notes = self.Notes(
            self.token, Collection(client, CardholderNoteResponseModel)
        )
        self.transitions = self.Transitions(
            self.token, Collection(client, UserTransitionResponse)
        )

    def ssn(self, full_ssn=False):
        """
        Provides SSN details
        :param full_ssn: set to True or False based on requirement
        :return: SsnResponseModel object
        """
        response = self.client.get(
            "users/{}/ssn".format(self.token), query_params={"full_ssn": full_ssn}
        )[0]
        return SsnResponseModel(response)

    class Children(object):
        """
        Lists the children for parent users
        Returns CardHolderModel object
        """

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(
                count=count,
                start_index=start_index,
                query_params=params,
                endpoint="users/{}/children".format(self.token),
            )

        def stream(self, params=None):
            return self.collection.stream(
                query_params=params, endpoint="users/{}/children".format(self.token)
            )

        def list(self, params=None, limit=None):
            return self.collection.list(
                query_params=params,
                endpoint="users/{}/children".format(self.token),
                limit=limit,
            )

        def __repr__(self):
            return "<Marqeta.resources.users.UsersContext.Children>"

    class Notes(object):
        """
        Lists, Creates and Updates the notes for users
        Returns CardholderNoteResponseModel object
        """

        _endpoint = "users/{}/notes"

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(
                endpoint=self._endpoint.format(self.token),
                count=count,
                start_index=start_index,
                query_params=params,
            )

        def stream(self, params=None):
            return self.collection.stream(
                endpoint=self._endpoint.format(self.token), query_params=params
            )

        def list(self, params=None, limit=None):
            return self.collection.list(
                endpoint=self._endpoint.format(self.token),
                query_params=params,
                limit=limit,
            )

        def create(self, data):
            return self.collection.create(
                data, endpoint=self._endpoint.format(self.token)
            )

        def save(self, notes_token, data):
            return self.collection.save(
                data,
                endpoint=self._endpoint.format(self.token) + "/{}".format(notes_token),
            )

        def __repr__(self):
            return "<Marqeta.resources.users.UsersContext.Notes>"

    class Transitions(object):
        """
        Lists, Creates and Finds the notes for users
        Returns UserTransitionResponse object
        """

        _endpoint = "usertransitions/user"

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0, params=None):
            return self.collection.page(
                count=count,
                start_index=start_index,
                query_params=params,
                endpoint=self._endpoint + "/{}".format(self.token),
            )

        def stream(self, params=None, limit=None):
            return self.collection.stream(
                query_params=params,
                endpoint=self._endpoint + "/{}".format(self.token),
                limit=limit,
            )

        def list(self, params=None, limit=None):
            return self.collection.list(
                query_params=params,
                endpoint=self._endpoint + "/{}".format(self.token),
                limit=limit,
            )

        def create(self, data):
            return self.collection.create(data, endpoint="usertransitions")

        def find(self, transition_token):
            return self.collection.find(
                endpoint="usertransitions/{}".format(transition_token)
            )

        def __repr__(self):
            return "<Marqeta.resources.users.UsersContext.Transitions>"

    def __repr__(self):
        return "<Marqeta.resources.users.UsersContext>"
