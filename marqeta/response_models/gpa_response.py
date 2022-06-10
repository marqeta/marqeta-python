from datetime import datetime, date
from marqeta.response_models.fee_detail import FeeDetail
from marqeta.response_models.response import Response
from marqeta.response_models.funding import Funding
from marqeta.response_models import datetime_object
import json
import re


class GpaResponse(object):
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
    def fees(self):
        if "fees" in self.json_response:
            return [FeeDetail(val) for val in self.json_response["fees"]]

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    @property
    def transaction_token(self):
        return self.json_response.get("transaction_token", None)

    @property
    def state(self):
        return self.json_response.get("state", None)

    @property
    def response(self):
        if "response" in self.json_response:
            return Response(self.json_response["response"])

    @property
    def funding(self):
        if "funding" in self.json_response:
            return Funding(self.json_response["funding"])

    @property
    def funding_source_token(self):
        return self.json_response.get("funding_source_token", None)

    @property
    def funding_source_address_token(self):
        return self.json_response.get("funding_source_address_token", None)

    @property
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def business_token(self):
        return self.json_response.get("business_token", None)

    @property
    def currency_code(self):
        return self.json_response.get("currency_code", None)

    @property
    def gateway_token(self):
        return self.json_response.get("gateway_token", None)

    @property
    def gateway_message(self):
        return self.json_response.get("gateway_message", None)

    def __repr__(self):
        return "<Marqeta.response_models.gpa_response.GpaResponse>" + self.__str__()
