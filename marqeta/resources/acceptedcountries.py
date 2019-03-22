from marqeta.resources.collection import Collection
from marqeta.response_models.accepted_countries_model import AcceptedCountriesModel


class AcceptedCountriesCollection(object):
    _endpoint = 'acceptedcountries'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, AcceptedCountriesModel)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the acceptedcountries  Returns list of all acceptedcountries object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a acceptedcountries with the specified data
            Returns the card product object which has created acceptedcountries information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the acceptedcountries information for the requested token
            Returns the cardproduct object which has acceptedcountries information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the acceptedcountries information for the requested token  with the data
                Returns the acceptedcountries object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.acceptedcountries.AcceptedCountriesCollection>'
