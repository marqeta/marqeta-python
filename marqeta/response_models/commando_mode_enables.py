from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class CommandoModeEnables(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def program_funding_source(self):
        return self.json_response.get('program_funding_source', None)


    @property
    def velocity_controls(self):
        return self.json_response.get('velocity_controls', None)

    @property
    def auth_controls(self):
        return self.json_response.get('auth_controls', None)

    @property
    def ignore_card_suspended_state(self):
        return self.json_response.get('ignore_card_suspended_state', None)

    def __repr__(self):
         return '<Marqeta.response_models.commando_mode_enables.CommandoModeEnables>' + self.__str__()
