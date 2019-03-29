from datetime import datetime, date
from marqeta.response_models.webhook_config_model import WebhookConfigModel
import json


class WebhookRequestModel(object):

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
    def name(self):

        return self.json_response.get('name', None)

    @property
    def active(self):

        return self.json_response.get('active', None)

    @property
    def config(self):

        if 'config' in self.json_response:
            return WebhookConfigModel(self.json_response['config'])

    @property
    def events(self):

        return self.json_response.get('events', None)

    def __repr__(self):
        return '<Marqeta.response_models.webhook_request_model.WebhookRequestModel>'
