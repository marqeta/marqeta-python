from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AddressVerification(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get("name", None)

    @property
    def street_address(self):
        return self.json_response.get("street_address", None)

    @property
    def zip(self):
        return self.json_response.get("zip", None)

    @property
    def postal_code(self):
        return self.json_response.get("postal_code", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.address_verification.AddressVerification>"
            + self.__str__()
        )
