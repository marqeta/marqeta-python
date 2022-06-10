from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class Available(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def uses(self):
        return self.json_response.get("uses", None)

    @property
    def amount(self):
        return self.json_response.get("amount", None)

    @property
    def days_remaining(self):
        return self.json_response.get("days_remaining", None)

    def __repr__(self):
        return "<Marqeta.response_models.available.Available>" + self.__str__()
