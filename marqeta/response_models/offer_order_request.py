from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class OfferOrderRequest(object):
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
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def business_token(self):
        return self.json_response.get("business_token", None)

    @property
    def offer_token(self):
        return self.json_response.get("offer_token", None)

    @property
    def funding_source_token(self):
        return self.json_response.get("funding_source_token", None)

    @property
    def funding_source_address_token(self):
        return self.json_response.get("funding_source_address_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.offer_order_request.OfferOrderRequest>"
            + self.__str__()
        )
