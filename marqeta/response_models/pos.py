from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class Pos(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pan_entry_mode(self):
        return self.json_response.get("pan_entry_mode", None)

    @property
    def pin_entry_mode(self):
        return self.json_response.get("pin_entry_mode", None)

    @property
    def terminal_id(self):
        return self.json_response.get("terminal_id", None)

    @property
    def terminal_attendance(self):
        return self.json_response.get("terminal_attendance", None)

    @property
    def terminal_location(self):
        return self.json_response.get("terminal_location", None)

    @property
    def card_holder_presence(self):
        return self.json_response.get("card_holder_presence", None)

    @property
    def cardholder_authentication_method(self):
        return self.json_response.get("cardholder_authentication_method", None)

    @property
    def card_presence(self):
        return self.json_response.get("card_presence", None)

    @property
    def terminal_type(self):
        return self.json_response.get("terminal_type", None)

    @property
    def card_data_input_capability(self):
        return self.json_response.get("card_data_input_capability", None)

    @property
    def country_code(self):
        return self.json_response.get("country_code", None)

    @property
    def zip(self):
        return self.json_response.get("zip", None)

    @property
    def partial_approval_capable(self):
        return self.json_response.get("partial_approval_capable", None)

    @property
    def purchase_amount_only(self):
        return self.json_response.get("purchase_amount_only", None)

    @property
    def is_recurring(self):
        return self.json_response.get("is_recurring", None)

    def __repr__(self):
        return "<Marqeta.response_models.pos.Pos>" + self.__str__()
