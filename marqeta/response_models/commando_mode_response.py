from datetime import datetime, date
from marqeta.response_models.commando_mode_nested_transition import CommandoModeNestedTransition
from marqeta.response_models.commando_mode_enables import CommandoModeEnables
from marqeta.response_models.real_time_standin_criteria import RealTimeStandinCriteria
import json


class CommandoModeResponse(object):

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
        return self.json_response.get('token', None)

    @property
    def program_gateway_funding_source_token(self):
        return self.json_response.get('program_gateway_funding_source_token', None)

    @property
    def current_state(self):
        if 'current_state' in self.json_response:
            return CommandoModeNestedTransition(self.json_response['current_state'])

    @property
    def commando_mode_enables(self):
        if 'commando_mode_enables' in self.json_response:
            return CommandoModeEnables(self.json_response['commando_mode_enables'])

    @property
    def real_time_standin_criteria(self):
        if 'real_time_standin_criteria' in self.json_response:
            return RealTimeStandinCriteria(self.json_response['real_time_standin_criteria'])

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.commando_mode_response.CommandoModeResponse>'
