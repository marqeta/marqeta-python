from datetime import datetime
from marqeta.response_models.webhook_config_model import WebhookConfigModel

class WebhookBaseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

