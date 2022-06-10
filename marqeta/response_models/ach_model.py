from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AchModel(object):
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
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def business_token(self):
        return self.json_response.get("business_token", None)

    @property
    def account_number(self):
        return self.json_response.get("account_number", None)

    @property
    def routing_number(self):
        return self.json_response.get("routing_number", None)

    @property
    def name_on_account(self):
        return self.json_response.get("name_on_account", None)

    @property
    def account_type(self):
        return self.json_response.get("account_type", None)

    @property
    def verification_override(self):
        return self.json_response.get("verification_override", None)

    @property
    def verification_notes(self):
        return self.json_response.get("verification_notes", None)

    @property
    def is_default_account(self):
        return self.json_response.get("is_default_account", None)

    def __repr__(self):
        return "<Marqeta.response_models.ach_model.AchModel>" + self.__str__()
