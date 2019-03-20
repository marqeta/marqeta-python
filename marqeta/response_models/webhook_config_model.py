from datetime import datetime, date
import json

class WebhookConfigModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def url(self):
        if 'url' in self.json_response:
            return self.json_response['url']

    @property
    def secret(self):
        if 'secret' in self.json_response:
            return self.json_response['secret']

    @property
    def basic_auth_username(self):
        if 'basic_auth_username' in self.json_response:
            return self.json_response['basic_auth_username']

    @property
    def basic_auth_password(self):
        if 'basic_auth_password' in self.json_response:
            return self.json_response['basic_auth_password']

    def __repr__(self):
         return '<Marqeta.response_models.webhook_config_model.WebhookConfigModel>'