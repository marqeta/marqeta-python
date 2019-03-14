from datetime import datetime, date
import json

class CommandoModeNestedTransition(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'commando_enabled' : self.commando_enabled,
           'reason' : self.reason,
           'channel' : self.channel,
           'username' : self.username,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def commando_enabled(self):
        if 'commando_enabled' in self.json_response:
            return self.json_response['commando_enabled']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def username(self):
        if 'username' in self.json_response:
            return self.json_response['username']

    def __repr__(self):
         return '<Marqeta.response_models.commando_mode_nested_transition.CommandoModeNestedTransition>'