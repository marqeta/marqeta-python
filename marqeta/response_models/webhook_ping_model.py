from datetime import datetime, date
from marqeta.response_models.echo_ping_request import EchoPingRequest
from marqeta.response_models import datetime_object
import json
import re


class WebhookPingModel(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pings(self):
        if "pings" in self.json_response:
            return [EchoPingRequest(val) for val in self.json_response["pings"]]

    def __repr__(self):
        return (
            "<Marqeta.response_models.webhook_ping_model.WebhookPingModel>"
            + self.__str__()
        )
