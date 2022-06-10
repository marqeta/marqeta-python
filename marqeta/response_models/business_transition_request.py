from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class BusinessTransitionRequest(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def idempotentHash(self):
        return self.json_response.get("idempotentHash", None)

    @property
    def token(self):
        return self.json_response.get("token", None)

    @property
    def status(self):
        return self.json_response.get("status", None)

    @property
    def reason_code(self):
        return self.json_response.get("reason_code", None)

    @property
    def reason(self):
        return self.json_response.get("reason", None)

    @property
    def channel(self):
        return self.json_response.get("channel", None)

    @property
    def business_token(self):
        return self.json_response.get("business_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.business_transition_request.BusinessTransitionRequest>"
            + self.__str__()
        )
