from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


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
        return self.json_response.get("endpoint", None)

    @property
    def username(self):
        return self.json_response.get("username", None)

    @property
    def password(self):
        return self.json_response.get("password", None)

    @property
    def secret(self):
        return self.json_response.get("secret", None)

    def __repr__(self):
        return "<Marqeta.response_models.webhook.Webhook>" + self.__str__()
