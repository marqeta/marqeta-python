"""User Card Holder Model with User Properties!!!"""

from datetime import datetime
from marqeta.response_models.authentication import Authentication
from marqeta.response_models.identification_response_model import IdentificationResponseModel
from marqeta.response_models.deposit_account import DepositAccount


class UserCardHolderResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def authentication(self):
        if 'authentication' in self.json_response:
            return Authentication(self.json_response['authentication'])

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def honorific(self):
        if 'honorific' in self.json_response:
            return self.json_response['honorific']

    @property
    def gender(self):
        if 'gender' in self.json_response:
            return self.json_response['gender']

    @property
    def first_name(self):
        if 'first_name' in self.json_response:
            return self.json_response['first_name']

    @property
    def middle_name(self):
        if 'middle_name' in self.json_response:
            return self.json_response['middle_name']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

    @property
    def address1(self):
        if 'address1' in self.json_response:
            return self.json_response['address1']

    @property
    def address2(self):
        if 'address2' in self.json_response:
            return self.json_response['address2']

    @property
    def city(self):
        if 'city' in self.json_response:
            return self.json_response['city']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def notes(self):
        if 'notes' in self.json_response:
            return self.json_response['notes']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def parent_token(self):
        if 'parent_token' in self.json_response:
            return self.json_response['parent_token']

    @property
    def uses_parent_account(self):
        if 'uses_parent_account' in self.json_response:
            return self.json_response['uses_parent_account']

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

    @property
    def corporate_card_holder(self):
        if 'corporate_card_holder' in self.json_response:
            return self.json_response['corporate_card_holder']

    @property
    def passport_number(self):
        if 'passport_number' in self.json_response:
            return self.json_response['passport_number']

    @property
    def id_card_number(self):
        if 'id_card_number' in self.json_response:
            return self.json_response['id_card_number']

    @property
    def nationality(self):
        if 'nationality' in self.json_response:
            return self.json_response['nationality']

    @property
    def company(self):
        if 'company' in self.json_response:
            return self.json_response['company']

    @property
    def ip_address(self):
        if 'ip_address' in self.json_response:
            return self.json_response['ip_address']

    @property
    def password(self):
        if 'password' in self.json_response:
            return self.json_response['password']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    @property
    def account_holder_group_token(self):
        if 'account_holder_group_token' in self.json_response:
            return self.json_response['account_holder_group_token']

    @property
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

    @property
    def identifications(self):
        if 'identifications' in self.json_response:
            return [IdentificationResponseModel(val) for val in self.json_response['identifications']]

    @property
    def deposit_account(self):
        if 'deposit_account' in self.json_response:
            return DepositAccount(self.json_response['deposit_account'])

    @property
    def birth_date(self):
        if 'birth_date' in self.json_response:
            return datetime.strptime(self.json_response['birth_date'], '%Y-%m-%d').date()

    @property
    def passport_expiration_date(self):
        if 'passport_expiration_date' in self.json_response:
            return datetime.strptime(self.json_response['passport_expiration_date'], '%Y-%m-%d').date()

    @property
    def id_card_expiration_date(self):
        if 'id_card_expiration_date' in self.json_response:
            return datetime.strptime(self.json_response['id_card_expiration_date'], '%Y-%m-%d').date()

