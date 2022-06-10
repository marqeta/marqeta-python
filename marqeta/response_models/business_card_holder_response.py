from datetime import datetime, date
from marqeta.response_models.authentication import Authentication
from marqeta.response_models.address_response_model import AddressResponseModel
from marqeta.response_models.primary_contact_info_model import PrimaryContactInfoModel
from marqeta.response_models.business_incorporation_response_model import (
    BusinessIncorporationResponseModel,
)
from marqeta.response_models.business_proprietor_response_model import (
    BusinessProprietorResponseModel,
)
from marqeta.response_models.identification_response_model import (
    IdentificationResponseModel,
)
from marqeta.response_models.deposit_account import DepositAccount
from marqeta.response_models import datetime_object
import json
import re


class BusinessCardHolderResponse(object):
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
    def active(self):
        return self.json_response.get("active", None)

    @property
    def notes(self):
        return self.json_response.get("notes", None)

    @property
    def ip_address(self):
        return self.json_response.get("ip_address", None)

    @property
    def password(self):
        return self.json_response.get("password", None)

    @property
    def phone(self):
        return self.json_response.get("phone", None)

    @property
    def metadata(self):
        return self.json_response.get("metadata", None)

    @property
    def account_holder_group_token(self):
        return self.json_response.get("account_holder_group_token", None)

    @property
    def authentication(self):
        if "authentication" in self.json_response:
            return Authentication(self.json_response["authentication"])

    @property
    def created_time(self):
        if "created_time" in self.json_response:
            return datetime_object("created_time", self.json_response)

    @property
    def last_modified_time(self):
        if "last_modified_time" in self.json_response:
            return datetime_object("last_modified_time", self.json_response)

    @property
    def status(self):
        return self.json_response.get("status", None)

    @property
    def business_name_legal(self):
        return self.json_response.get("business_name_legal", None)

    @property
    def business_name_dba(self):
        return self.json_response.get("business_name_dba", None)

    @property
    def office_location(self):
        if "office_location" in self.json_response:
            return AddressResponseModel(self.json_response["office_location"])

    @property
    def in_current_location_since(self):
        if "in_current_location_since" in self.json_response:
            return datetime_object("in_current_location_since", self.json_response)

    @property
    def website(self):
        return self.json_response.get("website", None)

    @property
    def date_established(self):
        if "date_established" in self.json_response:
            return datetime_object("date_established", self.json_response)

    @property
    def general_business_description(self):
        return self.json_response.get("general_business_description", None)

    @property
    def history(self):
        return self.json_response.get("history", None)

    @property
    def business_type(self):
        return self.json_response.get("business_type", None)

    @property
    def international_office_locations(self):
        return self.json_response.get("international_office_locations", None)

    @property
    def taxpayer_id(self):
        return self.json_response.get("taxpayer_id", None)

    @property
    def duns_number(self):
        return self.json_response.get("duns_number", None)

    @property
    def primary_contact(self):
        if "primary_contact" in self.json_response:
            return PrimaryContactInfoModel(self.json_response["primary_contact"])

    @property
    def incorporation(self):
        if "incorporation" in self.json_response:
            return BusinessIncorporationResponseModel(
                self.json_response["incorporation"]
            )

    @property
    def proprietor_or_officer(self):
        if "proprietor_or_officer" in self.json_response:
            return BusinessProprietorResponseModel(
                self.json_response["proprietor_or_officer"]
            )

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

    def __repr__(self):
        return (
            "<Marqeta.response_models.business_card_holder_response.BusinessCardHolderResponse>"
            + self.__str__()
        )
