from marqeta.resources.collection import Collection
from marqeta.response_models.program_transfer_response import ProgramTransferResponse
from marqeta.response_models.program_transfer_type_reponse import ProgramTransferTypeReponse


class ProgramTransfersCollection(object):
    _endpoint = 'programtransfers'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, ProgramTransferResponse)
        self.types = Types(Collection(client, ProgramTransferTypeReponse))

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the programtransfers  Returns list of all programtransfers object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a programtransfers with the specified data
            Returns the card product object which has created programtransfers information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the programtransfers information for the requested token
            Returns the cardproduct object which has programtransfers information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.programtransfers.Programtransfers>'


class Types(object):
    _endpoint = 'programtransfers/types'

    def __init__(self, collection):
        self.collections = collection

    def stream(self, params=None):
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the programtransfers/types  Returns list of all programtransfers/types object '''

    def list(self, params=None, limit=None):
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a programtransfers/types with the specified data
            Returns the card product object which has created programtransfers/types information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the programtransfers/types information for the requested token
            Returns the cardproduct object which has programtransfers/types information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the programtransfers/types information for the requested token  with the data
                Returns the programtransfers/types object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.programtransfers_types.ProgramtransfersTypes>'
