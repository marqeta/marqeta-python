from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class PeerTransferResponse(object):
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
    def amount(self):
        return self.json_response.get("amount", None)

    @property
    def tags(self):
        return self.json_response.get("tags", None)

    @property
    def memo(self):
        return self.json_response.get("memo", None)

    @property
    def currency_code(self):
        return self.json_response.get("currency_code", None)

    @property
    def sender_user_token(self):
        return self.json_response.get("sender_user_token", None)

    @property
    def recipient_user_token(self):
        return self.json_response.get("recipient_user_token", None)

    @property
    def sender_business_token(self):
        return self.json_response.get("sender_business_token", None)

    @property
    def recipient_business_token(self):
        return self.json_response.get("recipient_business_token", None)

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    def __repr__(self):
        return (
            "<Marqeta.response_models.peer_transfer_response.PeerTransferResponse>"
            + self.__str__()
        )
