from marqeta.resources.collection import Collection
from marqeta.response_models.auth_control_response import AuthControlResponse
from marqeta.response_models.auth_control_exempt_mids_response import AuthControlExemptMidsResponse


class AuthControlsCollection(object):
    _endpoint = 'authcontrols'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, AuthControlResponse)
        self.exempt_mids = AuthcontrolsExemptmidsCollection(self.client)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the authcontrols  Returns list of all authcontrols object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a authcontrols with the specified data
            Returns the card product object which has created authcontrols information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the authcontrols information for the requested token
            Returns the cardproduct object which has authcontrols information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the authcontrols information for the requested token  with the data
                Returns the authcontrols object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.authcontrols.AuthControlsCollection>'


class AuthcontrolsExemptmidsCollection(object):
    _endpoint = 'authcontrols/exemptmids'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, AuthControlExemptMidsResponse)

    def page(self, params=None):
        return self.collections.page(endpoint=self._endpoint, query_params=params)

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the authcontrols/exemptmids  Returns list of all authcontrols/exemptmids object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a authcontrols/exemptmids with the specified data
            Returns the card product object which has created authcontrols/exemptmids information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the authcontrols/exemptmids information for the requested token
            Returns the cardproduct object which has authcontrols/exemptmids information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the authcontrols/exemptmids information for the requested token  with the data
                Returns the authcontrols/exemptmids object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.authcontrols_exemptmids.AuthcontrolsExemptmidsCollection>'
