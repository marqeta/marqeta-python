from datetime import datetime, date
from marqeta.response_models.expiration_offset import ExpirationOffset
from marqeta.response_models.fulfillment import Fulfillment
from marqeta.response_models.activation_actions import ActivationActions
from marqeta.response_models import datetime_object
import json
import re


class CardRequest(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_product_token(self):
        return self.json_response.get("card_product_token", None)

    @property
    def expedite(self):
        return self.json_response.get("expedite", None)

    @property
    def metadata(self):
        return self.json_response.get("metadata", None)

    @property
    def expiration_offset(self):
        if "expiration_offset" in self.json_response:
            return ExpirationOffset(self.json_response["expiration_offset"])

    @property
    def token(self):
        return self.json_response.get("token", None)

    @property
    def user_token(self):
        return self.json_response.get("user_token", None)

    @property
    def fulfillment(self):
        if "fulfillment" in self.json_response:
            return Fulfillment(self.json_response["fulfillment"])

    @property
    def reissue_pan_from_card_token(self):
        return self.json_response.get("reissue_pan_from_card_token", None)

    @property
    def translate_pin_from_card_token(self):
        return self.json_response.get("translate_pin_from_card_token", None)

    @property
    def activation_actions(self):
        if "activation_actions" in self.json_response:
            return ActivationActions(self.json_response["activation_actions"])

    @property
    def bulk_issuance_token(self):
        return self.json_response.get("bulk_issuance_token", None)

    def __repr__(self):
        return "<Marqeta.response_models.card_request.CardRequest>" + self.__str__()
