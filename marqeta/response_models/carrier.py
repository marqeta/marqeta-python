from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class Carrier(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def template_id(self):
        return self.json_response.get("template_id", None)

    @property
    def logo_file(self):
        return self.json_response.get("logo_file", None)

    @property
    def logo_thumbnail_file(self):
        return self.json_response.get("logo_thumbnail_file", None)

    @property
    def message_file(self):
        return self.json_response.get("message_file", None)

    def __repr__(self):
        return "<Marqeta.response_models.carrier.Carrier>" + self.__str__()
