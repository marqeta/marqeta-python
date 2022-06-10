from datetime import datetime, date
from marqeta.response_models.fulfillment import Fulfillment
from marqeta.response_models import datetime_object
import json
import re


class CardUpdateRequest(object):
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
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def expedite(self):
        return self.json_response.get("expedite", None)

    @property
    def fulfillment(self):
        if "fulfillment" in self.json_response:
            return Fulfillment(self.json_response["fulfillment"])

    @property
    def metadata(self):
        return self.json_response.get("metadata", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.card_update_request.CardUpdateRequest>"
            + self.__str__()
        )
