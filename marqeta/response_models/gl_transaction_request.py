from datetime import datetime, date
from marqeta.response_models.gl_entry import GlEntry
from marqeta.response_models import datetime_object
import json
import re


class GlTransactionRequest(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def entries(self):
        if "entries" in self.json_response:
            return [GlEntry(val) for val in self.json_response["entries"]]

    @property
    def detail(self):
        return self.json_response.get("detail", None)

    @property
    def cardholder_visible(self):
        return self.json_response.get("cardholder_visible", None)

    @property
    def reference_transaction_token(self):
        return self.json_response.get("reference_transaction_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.gl_transaction_request.GlTransactionRequest>"
            + self.__str__()
        )
