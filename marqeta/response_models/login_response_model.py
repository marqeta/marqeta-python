from datetime import datetime
from marqeta.response_models.access_token_response import AccessTokenResponse
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse

class LoginResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def access_token(self):
        if 'access_token' in self.json_response:
            return AccessTokenResponse(self.json_response['access_token'])

    @property
    def user(self):
        if 'user' in self.json_response:
            return UserCardHolderResponse(self.json_response['user'])

