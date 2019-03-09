from datetime import datetime
from marqeta.response_models.avs_control_options import AvsControlOptions
from marqeta.response_models.avs_control_options import AvsControlOptions

class AvsControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def av_messages(self):
        if 'av_messages' in self.json_response:
            return AvsControlOptions(self.json_response['av_messages'])

    @property
    def auth_messages(self):
        if 'auth_messages' in self.json_response:
            return AvsControlOptions(self.json_response['auth_messages'])

