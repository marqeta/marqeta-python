from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class CardholderAuthenticationData(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def electronic_commerce_indicator(self):
        return self.json_response.get("electronic_commerce_indicator", None)

    @property
    def verification_result(self):
        return self.json_response.get("verification_result", None)

    @property
    def verification_value_created_by(self):
        return self.json_response.get("verification_value_created_by", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.cardholder_authentication_data.CardholderAuthenticationData>"
            + self.__str__()
        )
