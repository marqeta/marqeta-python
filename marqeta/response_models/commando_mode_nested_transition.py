from datetime import datetime

class CommandoModeNestedTransition(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

