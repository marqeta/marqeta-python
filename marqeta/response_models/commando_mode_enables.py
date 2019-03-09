from datetime import datetime

class CommandoModeEnables(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def program_funding_source(self):
        if 'program_funding_source' in self.json_response:
            return self.json_response['program_funding_source']

    @property
    def velocity_controls(self):
        if 'velocity_controls' in self.json_response:
            return self.json_response['velocity_controls']

    @property
    def auth_controls(self):
        if 'auth_controls' in self.json_response:
            return self.json_response['auth_controls']

    @property
    def ignore_card_suspended_state(self):
        if 'ignore_card_suspended_state' in self.json_response:
            return self.json_response['ignore_card_suspended_state']

