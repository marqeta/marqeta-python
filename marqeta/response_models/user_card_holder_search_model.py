from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class UserCardHolderSearchModel(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def ssn(self):
        return self.json_response.get("ssn", None)

    @property
    def dda(self):
        return self.json_response.get("dda", None)

    @property
    def first_name(self):
        return self.json_response.get("first_name", None)

    @property
    def last_name(self):
        return self.json_response.get("last_name", None)

    @property
    def phone(self):
        return self.json_response.get("phone", None)

    @property
    def email(self):
        return self.json_response.get("email", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.user_card_holder_search_model.UserCardHolderSearchModel>"
            + self.__str__()
        )
