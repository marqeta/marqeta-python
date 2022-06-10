from datetime import datetime, date
from marqeta.response_models.application import Application
from marqeta.response_models import datetime_object
import json
import re


class ClientAccessTokenResponse(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def application(self):
        if "application" in self.json_response:
            return Application(self.json_response["application"])

    @property
    def created(self):
        if "created" in self.json_response:
            return datetime_object("created", self.json_response)

    @property
    def expires(self):
        if "expires" in self.json_response:
            return datetime_object("expires", self.json_response)

    @property
    def token(self):
        return self.json_response.get("token", None)

    @property
    def card_token(self):
        return self.json_response.get("card_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.client_access_token_response.ClientAccessTokenResponse>"
            + self.__str__()
        )
