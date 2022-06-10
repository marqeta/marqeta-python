from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class Airline(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def passenger_name(self):
        return self.json_response.get("passenger_name", None)

    @property
    def depart_date(self):
        if "depart_date" in self.json_response:
            return datetime_object("depart_date", self.json_response)

    @property
    def origination_city(self):
        return self.json_response.get("origination_city", None)

    def __repr__(self):
        return "<Marqeta.response_models.airline.Airline>" + self.__str__()
