from datetime import datetime, date
from marqeta.response_models.commando_mode_nested_transition import CommandoModeNestedTransition
import json

class CommandoModeTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.commando_mode_transition_request.CommandoModeTransitionRequest>'