from datetime import datetime

class WebhookConfigModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

