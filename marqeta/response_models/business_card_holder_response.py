from datetime import datetime, date
from marqeta.response_models.authentication import Authentication
from marqeta.response_models.address_response_model import AddressResponseModel
from marqeta.response_models.primary_contact_info_model import PrimaryContactInfoModel
from marqeta.response_models.business_incorporation_response_model import BusinessIncorporationResponseModel
from marqeta.response_models.business_proprietor_response_model import BusinessProprietorResponseModel
from marqeta.response_models.identification_response_model import IdentificationResponseModel
from marqeta.response_models.deposit_account import DepositAccount
import json

class BusinessCardHolderResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'active' : self.active,
           'notes' : self.notes,
           'ip_address' : self.ip_address,
           'password' : self.password,
           'phone' : self.phone,
           'metadata' : self.metadata,
           'account_holder_group_token' : self.account_holder_group_token,
           'authentication' : self.authentication,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'status' : self.status,
           'business_name_legal' : self.business_name_legal,
           'business_name_dba' : self.business_name_dba,
           'office_location' : self.office_location,
           'in_current_location_since' : self.in_current_location_since,
           'website' : self.website,
           'date_established' : self.date_established,
           'general_business_description' : self.general_business_description,
           'history' : self.history,
           'business_type' : self.business_type,
           'international_office_locations' : self.international_office_locations,
           'taxpayer_id' : self.taxpayer_id,
           'duns_number' : self.duns_number,
           'primary_contact' : self.primary_contact,
           'incorporation' : self.incorporation,
           'proprietor_or_officer' : self.proprietor_or_officer,
           'identifications' : self.identifications,
           'deposit_account' : self.deposit_account,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def notes(self):
        if 'notes' in self.json_response:
            return self.json_response['notes']

    @property
    def ip_address(self):
        if 'ip_address' in self.json_response:
            return self.json_response['ip_address']

    @property
    def password(self):
        if 'password' in self.json_response:
            return self.json_response['password']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    @property
    def account_holder_group_token(self):
        if 'account_holder_group_token' in self.json_response:
            return self.json_response['account_holder_group_token']

    @property
    def authentication(self):
        if 'authentication' in self.json_response:
            return Authentication(self.json_response['authentication'])

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

    @property
    def business_name_legal(self):
        if 'business_name_legal' in self.json_response:
            return self.json_response['business_name_legal']

    @property
    def business_name_dba(self):
        if 'business_name_dba' in self.json_response:
            return self.json_response['business_name_dba']

    @property
    def office_location(self):
        if 'office_location' in self.json_response:
            return AddressResponseModel(self.json_response['office_location'])

    @property
    def in_current_location_since(self):
        if 'in_current_location_since' in self.json_response:
                return datetime.strptime(self.json_response['in_current_location_since'], '%Y-%m-%d').date()

    @property
    def website(self):
        if 'website' in self.json_response:
            return self.json_response['website']

    @property
    def date_established(self):
        if 'date_established' in self.json_response:
                return datetime.strptime(self.json_response['date_established'], '%Y-%m-%d').date()

    @property
    def general_business_description(self):
        if 'general_business_description' in self.json_response:
            return self.json_response['general_business_description']

    @property
    def history(self):
        if 'history' in self.json_response:
            return self.json_response['history']

    @property
    def business_type(self):
        if 'business_type' in self.json_response:
            return self.json_response['business_type']

    @property
    def international_office_locations(self):
        if 'international_office_locations' in self.json_response:
            return self.json_response['international_office_locations']

    @property
    def taxpayer_id(self):
        if 'taxpayer_id' in self.json_response:
            return self.json_response['taxpayer_id']

    @property
    def duns_number(self):
        if 'duns_number' in self.json_response:
            return self.json_response['duns_number']

    @property
    def primary_contact(self):
        if 'primary_contact' in self.json_response:
            return PrimaryContactInfoModel(self.json_response['primary_contact'])

    @property
    def incorporation(self):
        if 'incorporation' in self.json_response:
            return BusinessIncorporationResponseModel(self.json_response['incorporation'])

    @property
    def proprietor_or_officer(self):
        if 'proprietor_or_officer' in self.json_response:
            return BusinessProprietorResponseModel(self.json_response['proprietor_or_officer'])

    @property
    def identifications(self):
        if 'identifications' in self.json_response:
            return [IdentificationResponseModel(val) for val in self.json_response['identifications']]

    @property
    def deposit_account(self):
        if 'deposit_account' in self.json_response:
            return DepositAccount(self.json_response['deposit_account'])

    def __repr__(self):
         return '<Marqeta.response_models.business_card_holder_response.BusinessCardHolderResponse>'