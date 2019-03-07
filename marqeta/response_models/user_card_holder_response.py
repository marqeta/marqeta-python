"""User Card Holder Model with User Properties!!!"""

from datetime import datetime
from marqeta.response_models.authentication import Authentication
from marqeta.response_models.deposit_account import DepositAccount


class UserCardHolderResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def authentication(self):
        if 'authentication' in self.response:
            return Authentication(self.response['authentication'])

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def honorific(self):
        if 'honorific' in self.response:
            return self.response['honorific']

    @property
    def gender(self):
        if 'gender' in self.response:
            return self.response['gender']

    @property
    def first_name(self):
        if 'first_name' in self.response:
            return self.response['first_name']

    @property
    def middle_name(self):
        if 'middle_name' in self.response:
            return self.response['middle_name']

    @property
    def last_name(self):
        if 'last_name' in self.response:
            return self.response['last_name']

    @property
    def email(self):
        if 'email' in self.response:
            return self.response['email']

    @property
    def address1(self):
        if 'address1' in self.response:
            return self.response['address1']

    @property
    def address2(self):
        if 'address2' in self.response:
            return self.response['address2']

    @property
    def city(self):
        if 'city' in self.response:
            return self.response['city']

    @property
    def state(self):
        if 'state' in self.response:
            return self.response['state']

    @property
    def zip(self):
        if 'zip' in self.response:
            return self.response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.response:
            return self.response['postal_code']

    @property
    def country(self):
        if 'country' in self.response:
            return self.response['country']

    @property
    def notes(self):
        if 'notes' in self.response:
            return self.response['notes']

    @property
    def phone(self):
        if 'phone' in self.response:
            return self.response['phone']

    @property
    def parent_token(self):
        if 'parent_token' in self.response:
            return self.response['parent_token']

    @property
    def uses_parent_account(self):
        if 'uses_parent_account' in self.response:
            return self.response['uses_parent_account']

    @property
    def ssn(self):
        if 'ssn' in self.response:
            return self.response['ssn']

    @property
    def corporate_card_holder(self):
        if 'corporate_card_holder' in self.response:
            return self.response['corporate_card_holder']

    @property
    def passport_number(self):
        if 'passport_number' in self.response:
            return self.response['passport_number']

    @property
    def id_card_number(self):
        if 'id_card_number' in self.response:
            return self.response['id_card_number']

    @property
    def nationality(self):
        if 'nationality' in self.response:
            return self.response['nationality']

    @property
    def company(self):
        if 'company' in self.response:
            return self.response['company']

    @property
    def ip_address(self):
        if 'ip_address' in self.response:
            return self.response['ip_address']

    @property
    def password(self):
        if 'password' in self.response:
            return self.response['password']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def business_token(self):
        if 'business_token' in self.response:
            return self.response['business_token']

    @property
    def metadata(self):
        if 'metadata' in self.response:
            return self.response['metadata']

    @property
    def account_holder_group_token(self):
        if 'account_holder_group_token' in self.response:
            return self.response['account_holder_group_token']

    @property
    def status(self):
        if 'status' in self.response:
            return self.response['status']

    @property
    def identifications(self):
        if 'identifications' in self.response:
            return self.response['identifications']

    @property
    def deposit_account(self):
        if 'deposit_account' in self.response:
            return DepositAccount(self.response['deposit_account'])

    @property
    def birth_date(self):
        if 'birth_date' in self.response:
            return datetime.strptime(self.response['birth_date'], '%Y-%m-%d').date()

    @property
    def passport_expiration_date(self):
        if 'passport_expiration_date' in self.response:
            return datetime.strptime(self.response['passport_expiration_date'], '%Y-%m-%d').date()

    @property
    def id_card_expiration_date(self):
        if 'id_card_expiration_date' in self.response:
            return datetime.strptime(self.response['id_card_expiration_date'], '%Y-%m-%d').date()
