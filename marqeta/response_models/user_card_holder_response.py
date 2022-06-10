from datetime import datetime, date
from marqeta.response_models.authentication import Authentication
from marqeta.response_models.identification_response_model import (
    IdentificationResponseModel,
)
from marqeta.response_models.deposit_account import DepositAccount
from marqeta.response_models import datetime_object
import json
import re


class UserCardHolderResponse(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def authentication(self):
        if "authentication" in self.json_response:
            return Authentication(self.json_response["authentication"])

    @property
    def token(self):
        return self.json_response.get("token", None)

    @property
    def active(self):
        return self.json_response.get("active", None)

    @property
    def honorific(self):
        return self.json_response.get("honorific", None)

    @property
    def gender(self):
        return self.json_response.get("gender", None)

    @property
    def first_name(self):
        return self.json_response.get("first_name", None)

    @property
    def middle_name(self):
        return self.json_response.get("middle_name", None)

    @property
    def last_name(self):
        return self.json_response.get("last_name", None)

    @property
    def email(self):
        return self.json_response.get("email", None)

    @property
    def address1(self):
        return self.json_response.get("address1", None)

    @property
    def address2(self):
        return self.json_response.get("address2", None)

    @property
    def city(self):
        return self.json_response.get("city", None)

    @property
    def state(self):
        return self.json_response.get("state", None)

    @property
    def zip(self):
        return self.json_response.get("zip", None)

    @property
    def postal_code(self):
        return self.json_response.get("postal_code", None)

    @property
    def country(self):
        return self.json_response.get("country", None)

    @property
    def notes(self):
        return self.json_response.get("notes", None)

    @property
    def phone(self):
        return self.json_response.get("phone", None)

    @property
    def parent_token(self):
        return self.json_response.get("parent_token", None)

    @property
    def uses_parent_account(self):
        return self.json_response.get("uses_parent_account", None)

    @property
    def ssn(self):
        return self.json_response.get("ssn", None)

    @property
    def corporate_card_holder(self):
        return self.json_response.get("corporate_card_holder", None)

    @property
    def passport_number(self):
        return self.json_response.get("passport_number", None)

    @property
    def id_card_number(self):
        return self.json_response.get("id_card_number", None)

    @property
    def nationality(self):
        return self.json_response.get("nationality", None)

    @property
    def company(self):
        return self.json_response.get("company", None)

    @property
    def ip_address(self):
        return self.json_response.get("ip_address", None)

    @property
    def password(self):
        return self.json_response.get("password", None)

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    @property
    def business_token(self):
        return self.json_response.get("business_token", None)

    @property
    def metadata(self):
        return self.json_response.get("metadata", None)

    @property
    def account_holder_group_token(self):
        return self.json_response.get("account_holder_group_token", None)

    @property
    def status(self):
        return self.json_response.get("status", None)

    @property
    def identifications(self):
        if "identifications" in self.json_response:
            return [
                IdentificationResponseModel(val)
                for val in self.json_response["identifications"]
            ]

    @property
    def deposit_account(self):
        if "deposit_account" in self.json_response:
            return DepositAccount(self.json_response["deposit_account"])

    @property
    def birth_date(self):
        if "birth_date" in self.json_response:
            return datetime_object("birth_date", self.json_response)

    @property
    def passport_expiration_date(self):
        if "passport_expiration_date" in self.json_response:
            return datetime_object("passport_expiration_date", self.json_response)

    @property
    def id_card_expiration_date(self):
        if "id_card_expiration_date" in self.json_response:
            return datetime_object("id_card_expiration_date", self.json_response)

    def __repr__(self):
        return (
            "<Marqeta.response_models.user_card_holder_response.UserCardHolderResponse>"
            + self.__str__()
        )
