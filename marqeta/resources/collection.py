""" COLLECTION OF GENERIC CRU PARAMETERS """


class Collection(object):
    """
    Marqeta API -endpoint list, create, find and update operations
    """

    def __init__(self, client, resource):
        """
        Creates a client collection objects for different responses
        :param client: client object
        """
        self.client = client
        self.resource = resource

    def _page(self, **kwargs):
        """
        get the requested page from the API
        :param kwargs: requests arguments
        :return: the specified resource
        """
        return self.client.get(kwargs["endpoint"], query_params=kwargs["query_params"])[
            0
        ]

    def page(self, endpoint, count=5, start_index=0, query_params=None):
        """
        Provides the requested page for Endpoint
        :param endpoint: Endpoint
        :param count: data to be displayed per page
        :param start_index: start_index
        :param query_params: query parameters
        :return: requested page with resource object for the requested
        page 'data'field
        """
        params = {"count": count, "start_index": start_index}
        if query_params:
            params.update(query_params)
        response = self.client.get(endpoint, query_params=params)[0]
        for val in range(len(response["data"])):
            response["data"][val] = self.resource(response["data"][val])
        return response

    def stream(self, endpoint=None, query_params=None):
        """
        Stream is a generator function iterates through endpoint contents
        :param endpoint: Endpoint
        :param query_params: query parameters
        :return: resource object
        """
        params = {"count": 5, "start_index": 0}
        if query_params:
            params.update(query_params)
        while True:
            response = self._page(endpoint=endpoint, query_params=params)
            if response["is_more"] is False:
                for count in range(response["count"]):
                    yield self.resource(response["data"][count])
                break
            for count in range(response["count"]):
                yield self.resource(response["data"][count])
            params["start_index"] = params["start_index"] + params["count"]

    def list(self, endpoint=None, query_params=None, limit=None):
        """
        Lists the specified endpoint data field parameters
        :param endpoint: Endpoint
        :param query_params: query parameters
        :param limit: limit count for the list
        :return: list of resource object
        """
        list_of_user_object = []
        if limit == 0:
            return list_of_user_object
        for count in self.stream(endpoint=endpoint, query_params=query_params):
            list_of_user_object.append(count)
            if len(list_of_user_object) == limit:
                break
        return list_of_user_object

    def create(self, data, endpoint=None, query_params=None, proxy_data=None):
        """
        Creates an endpoint object
        :param data: data required for creation
        :param query_params: query parameters
        :param limit: limit count for the list
        :return: list of resource object
        """
        response = self.client.post(endpoint, data, query_params, proxy_data)[0]
        return self.resource(response)

    def find(self, endpoint=None, query_params=None):
        """
        Finds a specific endpoint object
        :param endpoint: Endpoint
        :param query_params: query parameters
        :return: list of resource object
        """
        response = self.client.get(endpoint, query_params=query_params)[0]
        return self.resource(response)

    def save(self, data, endpoint=None, proxy_data=None):
        """
        Updates an endpoint object
        :param data: data to be updated
        :param endpoint: Endpoint
        :return: resource object
        """
        response = self.client.put(endpoint, data, proxy_data)[0]
        return self.resource(response)

    def __repr__(self):
        return "<Marqeta.resources.collection.Collection>"
