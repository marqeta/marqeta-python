from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AcceptedCountriesModel(object):
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
    def is_whitelist(self):
        return self.json_response.get("is_whitelist", None)

    @property
    def country_codes(self):
        return self.json_response.get("country_codes", None)

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    def __repr__(self):
        return (
            "<Marqeta.response_models.accepted_countries_model.AcceptedCountriesModel>"
            + self.__str__()
        )
