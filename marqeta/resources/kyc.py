from marqeta.resources.collection import Collection
from marqeta.response_models.kyc_response import KycResponse


class KycCollection(object):
    _endpoint = 'kyc'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, KycResponse)

    def stream_for_user(self, user_token, params=None):
        return self.collections.stream(endpoint=self._endpoint + '/user/{}'.format(user_token), query_params=params)

    def stream_for_business(self, business_token, params=None):
        return self.collections.stream(endpoint=self._endpoint + '/business/{}'.format(business_token),
                                       query_params=params)

    def list_for_user(self, user_token, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint + '/user/{}'.format(user_token),
                                     query_params=params, limit=limit)

    def list_for_business(self, business_token, params=None,
                          limit=None):
        return self.collections.list(endpoint=self._endpoint + '/business/{}'.format(business_token),
                                     query_params=params, limit=limit)

    def create(self, data={}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.kyc.Kyc>'
