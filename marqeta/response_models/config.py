from datetime import datetime, date
from marqeta.response_models.authorization_controls import AuthorizationControls
import json


class Config(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def authorization_controls(self):

        if 'authorization_controls' in self.json_response:
            return AuthorizationControls(self.json_response['authorization_controls'])

    def __repr__(self):
        return '<Marqeta.response_models.config.Config>'
