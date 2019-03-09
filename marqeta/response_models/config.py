from datetime import datetime
from marqeta.response_models.authorization_controls import AuthorizationControls

class Config(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def authorization_controls(self):
        if 'authorization_controls' in self.json_response:
            return AuthorizationControls(self.json_response['authorization_controls'])

