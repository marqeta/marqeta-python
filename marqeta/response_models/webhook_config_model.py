from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


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
        return self.json_response.get("url", None)

    @property
    def secret(self):
        return self.json_response.get("secret", None)

    @property
    def basic_auth_username(self):
        return self.json_response.get("basic_auth_username", None)

    @property
    def basic_auth_password(self):
        return self.json_response.get("basic_auth_password", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.webhook_config_model.WebhookConfigModel>"
            + self.__str__()
        )
