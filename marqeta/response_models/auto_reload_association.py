from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AutoReloadAssociation(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_product_token(self):
        return self.json_response.get("card_product_token", None)

    @property
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def business_token(self):
        return self.json_response.get("business_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.auto_reload_association.AutoReloadAssociation>"
            + self.__str__()
        )
