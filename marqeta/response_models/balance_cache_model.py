from datetime import datetime, date
from marqeta.response_models.account_model import AccountModel
from marqeta.response_models import datetime_object
import json
import re


class BalanceCacheModel(object):
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
    def account(self):
        if "account" in self.json_response:
            return AccountModel(self.json_response["account"])

    @property
    def balance(self):
        return self.json_response.get("balance", None)

    @property
    def layers(self):
        return self.json_response.get("layers", None)

    @property
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    def __repr__(self):
        return (
            "<Marqeta.response_models.balance_cache_model.BalanceCacheModel>"
            + self.__str__()
        )
