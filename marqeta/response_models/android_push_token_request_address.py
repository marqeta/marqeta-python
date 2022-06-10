from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AndroidPushTokenRequestAddress(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get("name", None)

    @property
    def address1(self):
        return self.json_response.get("address1", None)

    @property
    def address2(self):
        return self.json_response.get("address2", None)

    @property
    def city(self):
        return self.json_response.get("city", None)

    @property
    def state(self):
        return self.json_response.get("state", None)

    @property
    def zip(self):
        return self.json_response.get("zip", None)

    @property
    def postal_code(self):
        return self.json_response.get("postal_code", None)

    @property
    def country(self):
        return self.json_response.get("country", None)

    @property
    def phone(self):
        return self.json_response.get("phone", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.android_push_token_request_address.AndroidPushTokenRequestAddress>"
            + self.__str__()
        )
