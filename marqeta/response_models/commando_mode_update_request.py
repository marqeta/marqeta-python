from datetime import datetime, date
from marqeta.response_models.real_time_standin_criteria import RealTimeStandinCriteria
from marqeta.response_models.commando_mode_enables import CommandoModeEnables
import json


class CommandoModeUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def program_gateway_funding_source_token(self):
        return self.json_response.get('program_gateway_funding_source_token', None)

    @property
    def real_time_standin_criteria(self):
      if 'real_time_standin_criteria' in self.json_response:
            return RealTimeStandinCriteria(self.json_response['real_time_standin_criteria'])

    @property
    def commando_mode_enables(self):
        if 'commando_mode_enables' in self.json_response:
            return CommandoModeEnables(self.json_response['commando_mode_enables'])

    def __repr__(self):
        return '<Marqeta.response_models.commando_mode_update_request.CommandoModeUpdateRequest>' + self.__str__()
