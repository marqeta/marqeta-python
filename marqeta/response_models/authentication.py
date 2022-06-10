from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class Authentication(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def last_password_update_channel(self):
        return self.json_response.get("last_password_update_channel", None)

    @property
    def last_password_update_time(self):
        if "last_password_update_time" in self.json_response:
            return datetime_object("last_password_update_time", self.json_response)

    @property
    def email_verified(self):
        return self.json_response.get("email_verified", None)

    @property
    def email_verified_time(self):
        if "email_verified_time" in self.json_response:
            return datetime_object("email_verified_time", self.json_response)

    def __repr__(self):
        return (
            "<Marqeta.response_models.authentication.Authentication>" + self.__str__()
        )
