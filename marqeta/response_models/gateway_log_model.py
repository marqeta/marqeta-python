from datetime import datetime, date
from marqeta.response_models.gateway_response import GatewayResponse
from marqeta.response_models import datetime_object
import json
import re


class GatewayLogModel(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def order_number(self):
        return self.json_response.get("order_number", None)

    @property
    def transaction_id(self):
        return self.json_response.get("transaction_id", None)

    @property
    def message(self):
        return self.json_response.get("message", None)

    @property
    def duration(self):
        return self.json_response.get("duration", None)

    @property
    def timed_out(self):
        return self.json_response.get("timed_out", None)

    @property
    def response(self):
        if "response" in self.json_response:
            return GatewayResponse(self.json_response["response"])

    def __repr__(self):
        return (
            "<Marqeta.response_models.gateway_log_model.GatewayLogModel>"
            + self.__str__()
        )
