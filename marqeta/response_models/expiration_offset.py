from datetime import datetime, date
from marqeta.response_models.min_offset import MinOffset
from marqeta.response_models import datetime_object
import json
import re


class ExpirationOffset(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def unit(self):
        return self.json_response.get("unit", None)

    @property
    def value(self):
        return self.json_response.get("value", None)

    @property
    def min_offset(self):
        if "min_offset" in self.json_response:
            return MinOffset(self.json_response["min_offset"])

    def __repr__(self):
        return (
            "<Marqeta.response_models.expiration_offset.ExpirationOffset>"
            + self.__str__()
        )
