from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class GlEntry(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def detail(self):
        return self.json_response.get("detail", None)

    @property
    def tag(self):
        return self.json_response.get("tag", None)

    @property
    def amount(self):
        return self.json_response.get("amount", None)

    @property
    def layer(self):
        return self.json_response.get("layer", None)

    @property
    def account(self):
        return self.json_response.get("account", None)

    @property
    def type(self):
        return self.json_response.get("type", None)

    def __repr__(self):
        return "<Marqeta.response_models.gl_entry.GlEntry>" + self.__str__()
