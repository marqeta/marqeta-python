from datetime import datetime, date
from marqeta.response_models.card_product_config import CardProductConfig
from marqeta.response_models import datetime_object
import json
import re


class CardProductRequest(object):
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
    def name(self):
        return self.json_response.get("name", None)

    @property
    def active(self):
        return self.json_response.get("active", None)

    @property
    def start_date(self):
        if "start_date" in self.json_response:
            return datetime_object("start_date", self.json_response)

    @property
    def end_date(self):
        if "end_date" in self.json_response:
            return datetime_object("end_date", self.json_response)

    @property
    def config(self):
        if "config" in self.json_response:
            return CardProductConfig(self.json_response["config"])

    def __repr__(self):
        return (
            "<Marqeta.response_models.card_product_request.CardProductRequest>"
            + self.__str__()
        )
