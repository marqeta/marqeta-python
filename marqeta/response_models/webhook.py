from datetime import datetime

class Webhook(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def endpoint(self):
        if 'endpoint' in self.json_response:
            return self.json_response['endpoint']

    @property
    def username(self):
        if 'username' in self.json_response:
            return self.json_response['username']

    @property
    def password(self):
        if 'password' in self.json_response:
            return self.json_response['password']

    @property
    def secret(self):
        if 'secret' in self.json_response:
            return self.json_response['secret']

