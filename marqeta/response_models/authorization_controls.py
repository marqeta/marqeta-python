from datetime import datetime, date
from marqeta.response_models.hold_increase import HoldIncrease
from marqeta.response_models import datetime_object
import json
import re


class AuthorizationControls(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def hold_increase(self):
        if "hold_increase" in self.json_response:
            return HoldIncrease(self.json_response["hold_increase"])

    @property
    def hold_expiration_days(self):
        return self.json_response.get("hold_expiration_days", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.authorization_controls.AuthorizationControls>"
            + self.__str__()
        )
