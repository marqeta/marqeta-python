from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class ChargebackTransitionResponse(object):
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
    def state(self):
        return self.json_response.get("state", None)

    @property
    def previous_state(self):
        return self.json_response.get("previous_state", None)

    @property
    def channel(self):
        return self.json_response.get("channel", None)

    @property
    def chargeback_token(self):
        return self.json_response.get("chargeback_token", None)

    @property
    def reason(self):
        return self.json_response.get("reason", None)

    @property
    def transaction_token(self):
        return self.json_response.get("transaction_token", None)

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    @property
    def type(self):
        return self.json_response.get("type", None)

    @property
    def amount(self):
        return self.json_response.get("amount", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.chargeback_transition_response.ChargebackTransitionResponse>"
            + self.__str__()
        )
