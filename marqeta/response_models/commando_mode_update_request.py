from datetime import datetime
from marqeta.response_models.real_time_standin_criteria import RealTimeStandinCriteria
from marqeta.response_models.commando_mode_enables import CommandoModeEnables

class CommandoModeUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def program_gateway_funding_source_token(self):
        if 'program_gateway_funding_source_token' in self.json_response:
            return self.json_response['program_gateway_funding_source_token']

    @property
    def real_time_standin_criteria(self):
        if 'real_time_standin_criteria' in self.json_response:
            return RealTimeStandinCriteria(self.json_response['real_time_standin_criteria'])

    @property
    def commando_mode_enables(self):
        if 'commando_mode_enables' in self.json_response:
            return CommandoModeEnables(self.json_response['commando_mode_enables'])

