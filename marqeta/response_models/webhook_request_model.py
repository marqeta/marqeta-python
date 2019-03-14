from datetime import datetime, date
from marqeta.response_models.webhook_config_model import WebhookConfigModel
import json

class WebhookRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'name' : self.name,
           'active' : self.active,
           'config' : self.config,
           'events' : self.events,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def config(self):
        if 'config' in self.json_response:
            return WebhookConfigModel(self.json_response['config'])

    @property
    def events(self):
        if 'events' in self.json_response:
            return self.json_response['events']

    def __repr__(self):
         return '<Marqeta.response_models.webhook_request_model.WebhookRequestModel>'