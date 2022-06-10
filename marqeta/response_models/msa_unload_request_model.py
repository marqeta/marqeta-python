from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class MsaUnloadRequestModel(object):
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

    def __repr__(self):
        return (
            "<Marqeta.response_models.msa_unload_request_model.MsaUnloadRequestModel>"
            + self.__str__()
        )
