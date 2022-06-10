from datetime import datetime, date
from marqeta.response_models.auto_reload_association import AutoReloadAssociation
from marqeta.response_models.order_scope import OrderScope
from marqeta.response_models import datetime_object
import json
import re


class AutoReloadResponseModel(object):
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
    def active(self):
        return self.json_response.get("active", None)

    @property
    def funding_source_token(self):
        return self.json_response.get("funding_source_token", None)

    @property
    def funding_source_address_token(self):
        return self.json_response.get("funding_source_address_token", None)

    @property
    def association(self):
        if "association" in self.json_response:
            return AutoReloadAssociation(self.json_response["association"])

    @property
    def order_scope(self):
        if "order_scope" in self.json_response:
            return OrderScope(self.json_response["order_scope"])

    @property
    def currency_code(self):
        return self.json_response.get("currency_code", None)

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
            "<Marqeta.response_models.auto_reload_response_model.AutoReloadResponseModel>"
            + self.__str__()
        )
