from datetime import datetime, date
import json

class CommandoModeEnables(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'program_funding_source' : self.program_funding_source,
           'velocity_controls' : self.velocity_controls,
           'auth_controls' : self.auth_controls,
           'ignore_card_suspended_state' : self.ignore_card_suspended_state,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.commando_mode_enables.CommandoModeEnables>'