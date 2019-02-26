"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime


class UserResource(object):

    def __init__(self, user_object):
        self.response = user_object

    @property
    def first_name(self):
        return self.response['first_name']

    @property
    def last_name(self):
        return self.response['last_name']

    @property
    def token(self):
        return self.response['token']

    @property
    def active(self):
        return self.response['active']

    @property
    def gender(self):
        return self.response['gender']

    @property
    def email(self):
        return self.response['email']

    @property
    def phone(self):
        return self.response['phone']

    @property
    def address(self):
        return Address(self.response)

    @property
    def uses_parent_account(self):
        return self.response['uses_parent_account']

    @property
    def corporate_card_holder(self):
        return self.response['corporate_card_holder']

    @property
    def created_time(self):
        return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def metadata(self):
        return self.response['metadata']

    @property
    def birth_date(self):
        return datetime.strptime(self.response['birth_date'], '%Y-%m-%d').date()

    @property
    def account_holder_group_token(self):
        return self.response['account_holder_group_token']

    @property
    def status(self):
        return self.response['status']

    @property
    def id_card_expiration_date(self):
        return datetime.strptime(self.response['id_card_expiration_date'], '%Y-%m-%d').date()

    @property
    def notes(self):
        return self.response['notes']

    @property
    def ip_address(self):
        return self.response['password']

    @property
    def company(self):
        return self.response['company']

    @property
    def honorific(self):
        return self.response['honorific']

    @property
    def middle_name(self):
        return self.response['middle_name']

    @property
    def nationality(self):
        return self.response['nationality']

    @property
    def passport_number(self):
        return self.response['passport_number']

    @property
    def passport_expiration_date(self):
        return datetime.strptime(self.response['passport_expiration_date'], '%Y-%m-%d').date()

    @property
    def id_card_number(self):
        return self.response['id_card_number']

    @property
    def parent_token(self):
        return self.response['parent_token']

    @property
    def authentication(self):

        return Authentication(self.response['auth_details'])

    @property
    def ssn(self):
        id_details = self.response['ssn']
        return id_details

    @property
    def deposit_account(self):

        account_info = self.response['deposit_account']
        return DepositAccount(account_info)


class Address(object):

    def __init__(self, response):
        self.response = response

    @property
    def address1(self):
        return self.response['address1']

    @property
    def address2(self):
        return self.response['address2']

    @property
    def state(self):
        return self.response['state']

    @property
    def city(self):
        return self.response['city']

    @property
    def country(self):
        return self.response['country']

    @property
    def postal_code(self):
        return self.response['postal_code']


class DepositAccount(object):

    def __init__(self, account_details):
        self.account_details = account_details

    @property
    def account_number(self):
        return self.account_details['account_number']

    @property
    def routing_number(self):
        return self.account_details['routing_number']

    @property
    def allow_immediate_credit(self):
        return self.account_details['allow_immediate_credit']

    @property
    def token(self):
        return self.account_details['token']

    @property
    def user_token(self):
        return self.account_details['user_token']

    @property
    def business_token(self):
        return self.account_details['business_token']


class Authentication(object):

    def __init__(self, auth_details):
        self.auth_details = auth_details

    @property
    def last_password_update_channel(self):
        return self.auth_details['last_password_update_channel']

    @property
    def last_password_update_time(self):
        return datetime.strptime(self.auth_details['last_password_update_time'],
                                 '%Y-%m-%dT%H:%M:%SZ')
    @property
    def email_verified(self):
        return self.auth_details['email_verified']

    @property
    def email_verified_time(self):
        return datetime.strptime(self.auth_details['email_verified_time'],
                                 '%Y-%m-%dT%H:%M:%SZ')


class NotesResources(object):

    def __init__(self, user_object):
        self.response = user_object

    @property
    def token(self):
        return self.response['token']

    @property
    def description(self):
        return self.response['description']

    @property
    def created_by(self):
        return self.response['created_by']

    @property
    def created_by_user_role(self):
        return self.response['created_by_user_role']

    @property
    def private(self):
        return self.response['private']

    @property
    def created_time(self):
        return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')


class TransitionsResources(object):

    def __init__(self, user_object):
        self.response = user_object

    @property
    def token(self):
        return self.response['token']

    @property
    def status(self):
        return self.response['status']

    @property
    def reason_code(self):
        return self.response['reason_code']

    @property
    def reason(self):
        return self.response['reason']

    @property
    def channel(self):
        return self.response['channel']

    @property
    def created_time(self):
        return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def user_token(self):
        return self.response['user_token']
