from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AccountModel(object):
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
    def code(self):
        return self.json_response.get("code", None)

    @property
    def description(self):
        return self.json_response.get("description", None)

    def __repr__(self):
        return "<Marqeta.response_models.account_model.AccountModel>" + self.__str__()
