from marqeta.resources.collection import Collection
from marqeta.response_models.push_to_card_disbursement_response import PushToCardDisbursementResponse
from marqeta.response_models.push_to_card_response import PushToCardResponse


class PushtocardsCollection(object):

    def __init__(self, client):
        self.client = client

        self.collections_pushtocards = Collection(self.client, PushtocardsPaymentcardCollection)
        self.disburse = PushtocardsDisburseCollection(self.client)
        self.payment_card = PushtocardsPaymentcardCollection(self.client)


class PushtocardsDisburseCollection(object):
    _endpoint = 'pushtocards/disburse'

    def __init__(self, client):
        self.client = client
        self.collections_disburse = Collection(self.client, PushToCardDisbursementResponse)

    def stream(self, params=None):
        return self.collections_disburse.stream(endpoint=self._endpoint, query_params=params)

    ''' Lists all the pushtocards/disburse  Returns list of all pushtocards/disburse object '''

    def list(self, params=None, limit=float('inf')):
        return self.collections_disburse.list(endpoint=self._endpoint, query_params=params, limit=limit)

    ''' Create a pushtocards/disburse with the specified data
            Returns the card product object which has created pushtocards/disburse information'''

    def create(self, data, params=None):
        return self.collections_disburse.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the pushtocards/disburse information for the requested token
            Returns the cardproduct object which has pushtocards/disburse information '''

    def find(self, token, params=None):
        return self.collections_disburse.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the pushtocards/disburse information for the requested token  with the data
                Returns the pushtocards/disburse object which has updated user information'''

    def save(self, token, data):
        return self.collections_disburse.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.pushtocards.PushtocardsDisburseCollection>'


class PushtocardsPaymentcardCollection(object):
    _endpoint = 'pushtocards/paymentcard'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, PushToCardResponse)

    def stream_for_user(self,token,  params=None):
        query_params = {'user_token': token}
        if params is not None:
            query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint, query_params=query_params)

    ''' Lists all the pushtocards/paymentcard  Returns list of all pushtocards/paymentcard object '''

    def list_for_user(self, token, params=None, limit=float('inf')):
        query_params = {'user_token': token}
        if params is not None:
            query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=query_params, limit=limit)

    ''' Create a pushtocards/paymentcard with the specified data
            Returns the card product object which has created pushtocards/paymentcard information'''

    def create(self, data, params=None):
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    ''' Finds the pushtocards/paymentcard information for the requested token
            Returns the cardproduct object which has pushtocards/paymentcard information '''

    def find(self, token, params=None):
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token), query_params=params)

    ''' Update the pushtocards/paymentcard information for the requested token  with the data
                Returns the pushtocards/paymentcard object which has updated user information'''

    def save(self, token, data):
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.pushtocards.PushtocardsPaymentcardCollection>'
