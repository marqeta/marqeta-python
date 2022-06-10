from datetime import datetime, date
from marqeta.response_models.application import Application
from marqeta.response_models import datetime_object
import json
import re


class AccessTokenResponse(object):
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
        return self.json_response.get("token", None)

    @property
    def expires(self):
        if "expires" in self.json_response:
            return datetime_object("expires", self.json_response)

    @property
    def application(self):
        if "application" in self.json_response:
            return Application(self.json_response["application"])

    @property
    def tokenTypeMarqetaMaster(self):
        return self.json_response.get("tokenTypeMarqetaMaster", None)

    @property
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def master_roles(self):
        return self.json_response.get("master_roles", None)

    @property
    def token_type(self):
        return self.json_response.get("token_type", None)

    @property
    def one_time(self):
        return self.json_response.get("one_time", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.access_token_response.AccessTokenResponse>"
            + self.__str__()
        )
