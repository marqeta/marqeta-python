from datetime import datetime, date
from marqeta.response_models.identification_request_model import IdentificationRequestModel
import json


class CardHolderModel(object):

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
        return self.json_response.get('token', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def notes(self):
        return self.json_response.get('notes', None)

    @property
    def ip_address(self):
        return self.json_response.get('ip_address', None)

    @property
    def password(self):
        return self.json_response.get('password', None)

    @property
    def phone(self):
        return self.json_response.get('phone', None)

    @property
    def metadata(self):
        return self.json_response.get('metadata', None)

    @property
    def account_holder_group_token(self):
        return self.json_response.get('account_holder_group_token', None)

    @property
    def identifications(self):
        if 'identifications' in self.json_response:
            return [IdentificationRequestModel(val) for val in self.json_response['identifications']]

    @property
    def honorific(self):
        return self.json_response.get('honorific', None)

    @property
    def gender(self):
        return self.json_response.get('gender', None)

    @property
    def first_name(self):
        return self.json_response.get('first_name', None)

    @property
    def middle_name(self):
        return self.json_response.get('middle_name', None)

    @property
    def last_name(self):
        return self.json_response.get('last_name', None)

    @property
    def email(self):
        return self.json_response.get('email', None)

    @property
    def address1(self):
        return self.json_response.get('address1', None)

    @property
    def address2(self):
        return self.json_response.get('address2', None)

    @property
    def city(self):
        return self.json_response.get('city', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def country(self):
        return self.json_response.get('country', None)

    @property
    def birth_date(self):
        return self.json_response.get('birth_date', None)

    @property
    def corporate_card_holder(self):
        return self.json_response.get('corporate_card_holder', None)

    @property
    def ssn(self):
        return self.json_response.get('ssn', None)

    @property
    def passport_number(self):
        return self.json_response.get('passport_number', None)

    @property
    def passport_expiration_date(self):
        return self.json_response.get('passport_expiration_date', None)

    @property
    def id_card_number(self):
        return self.json_response.get('id_card_number', None)

    @property
    def id_card_expiration_date(self):
        return self.json_response.get('id_card_expiration_date', None)

    @property
    def nationality(self):
        return self.json_response.get('nationality', None)

    @property
    def company(self):
        return self.json_response.get('company', None)

    @property
    def parent_token(self):
        return self.json_response.get('parent_token', None)

    @property
    def uses_parent_account(self):
        return self.json_response.get('uses_parent_account', None)

    @property
    def postal_code(self):
        return self.json_response.get('postal_code', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_holder_model.CardHolderModel>' + self.__str__()
