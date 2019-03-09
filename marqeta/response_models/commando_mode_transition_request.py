from datetime import datetime
from marqeta.response_models.commando_mode_nested_transition import CommandoModeNestedTransition

class CommandoModeTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def commando_mode_token(self):
        if 'commando_mode_token' in self.json_response:
            return self.json_response['commando_mode_token']

    @property
    def transition(self):
        if 'transition' in self.json_response:
            return CommandoModeNestedTransition(self.json_response['transition'])

