from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class CommandoModeNestedTransition(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def commando_enabled(self):
        return self.json_response.get("commando_enabled", None)

    @property
    def reason(self):
        return self.json_response.get("reason", None)

    @property
    def channel(self):
        return self.json_response.get("channel", None)

    @property
    def username(self):
        return self.json_response.get("username", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.commando_mode_nested_transition.CommandoModeNestedTransition>"
            + self.__str__()
        )
