from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class UnloadRequestModel(object):
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
    def original_order_token(self):
        return self.json_response.get("original_order_token", None)

    @property
    def amount(self):
        return self.json_response.get("amount", None)

    @property
    def tags(self):
        return self.json_response.get("tags", None)

    @property
    def memo(self):
        return self.json_response.get("memo", None)

    @property
    def funding_source_address_token(self):
        return self.json_response.get("funding_source_address_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.unload_request_model.UnloadRequestModel>"
            + self.__str__()
        )
