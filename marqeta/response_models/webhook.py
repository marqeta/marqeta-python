from datetime import datetime, date
import json

class Webhook(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.webhook.Webhook>'