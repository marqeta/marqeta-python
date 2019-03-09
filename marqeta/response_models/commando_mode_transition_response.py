from datetime import datetime
from marqeta.response_models.commando_mode_nested_transition import CommandoModeNestedTransition

class CommandoModeTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

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

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

