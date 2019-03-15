from datetime import datetime, date
from marqeta.response_models.access_token_response import AccessTokenResponse
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse
import json

class LoginResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'access_token' : self.access_token,
           'user' : self.user,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def access_token(self):
        if 'access_token' in self.json_response:
            return AccessTokenResponse(self.json_response['access_token'])

    @property
    def user(self):
        if 'user' in self.json_response:
            return UserCardHolderResponse(self.json_response['user'])

    def __repr__(self):
         return '<Marqeta.response_models.login_response_model.LoginResponseModel>'