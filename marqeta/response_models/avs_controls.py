from datetime import datetime, date
from marqeta.response_models.avs_control_options import AvsControlOptions
from marqeta.response_models.avs_control_options import AvsControlOptions
import json

class AvsControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'av_messages' : self.av_messages,
           'auth_messages' : self.auth_messages,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def av_messages(self):
        if 'av_messages' in self.json_response:
            return AvsControlOptions(self.json_response['av_messages'])

    @property
    def auth_messages(self):
        if 'auth_messages' in self.json_response:
            return AvsControlOptions(self.json_response['auth_messages'])

    def __repr__(self):
         return '<Marqeta.response_models.avs_controls.AvsControls>'