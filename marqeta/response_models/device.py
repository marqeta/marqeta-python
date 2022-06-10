from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class Device(object):
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
    def type(self):
        return self.json_response.get("type", None)

    @property
    def language_code(self):
        return self.json_response.get("language_code", None)

    @property
    def device_id(self):
        return self.json_response.get("device_id", None)

    @property
    def phone_number(self):
        return self.json_response.get("phone_number", None)

    @property
    def name(self):
        return self.json_response.get("name", None)

    @property
    def location(self):
        return self.json_response.get("location", None)

    @property
    def ip_address(self):
        return self.json_response.get("ip_address", None)

    def __repr__(self):
        return "<Marqeta.response_models.device.Device>" + self.__str__()
