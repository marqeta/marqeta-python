from datetime import datetime, date
from marqeta.response_models.android_push_token_request_address import (
    AndroidPushTokenRequestAddress,
)
from marqeta.response_models import datetime_object
import json
import re


class PushTokenizeRequestData(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def display_name(self):
        return self.json_response.get("display_name", None)

    @property
    def last_digits(self):
        return self.json_response.get("last_digits", None)

    @property
    def network(self):
        return self.json_response.get("network", None)

    @property
    def token_service_provider(self):
        return self.json_response.get("token_service_provider", None)

    @property
    def opaque_payment_card(self):
        return self.json_response.get("opaque_payment_card", None)

    @property
    def user_address(self):
        if "user_address" in self.json_response:
            return AndroidPushTokenRequestAddress(self.json_response["user_address"])

    def __repr__(self):
        return (
            "<Marqeta.response_models.push_tokenize_request_data.PushTokenizeRequestData>"
            + self.__str__()
        )
