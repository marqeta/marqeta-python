from datetime import datetime, date
from marqeta.response_models.spend_control_association import SpendControlAssociation
from marqeta.response_models.merchant_scope import MerchantScope
from marqeta.response_models import datetime_object
import json
import re


class AuthControlRequest(object):
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
    def association(self):
        if "association" in self.json_response:
            return SpendControlAssociation(self.json_response["association"])

    @property
    def merchant_scope(self):
        if "merchant_scope" in self.json_response:
            return MerchantScope(self.json_response["merchant_scope"])

    @property
    def start_time(self):
        if "start_time" in self.json_response:
            return datetime_object("start_time", self.json_response)

    @property
    def end_time(self):
        if "end_time" in self.json_response:
            return datetime_object("end_time", self.json_response)

    @property
    def active(self):
        return self.json_response.get("active", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.auth_control_request.AuthControlRequest>"
            + self.__str__()
        )
