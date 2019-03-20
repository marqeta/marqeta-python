from datetime import datetime, date
from marqeta.response_models.identification_request_model import IdentificationRequestModel
from marqeta.response_models.address_request_model import AddressRequestModel
from marqeta.response_models.primary_contact_info_model import PrimaryContactInfoModel
from marqeta.response_models.business_incorporation_request_model import BusinessIncorporationRequestModel
from marqeta.response_models.business_proprietor_request_model import BusinessProprietorRequestModel
import json

class BusinessCardHolderModel(object):

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
    def identifications(self):
        if 'identifications' in self.json_response:
            return [IdentificationRequestModel(val) for val in self.json_response['identifications']]

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
            return AddressRequestModel(self.json_response['office_location'])

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
            return BusinessIncorporationRequestModel(self.json_response['incorporation'])

    @property
    def proprietor_or_officer(self):
        if 'proprietor_or_officer' in self.json_response:
            return BusinessProprietorRequestModel(self.json_response['proprietor_or_officer'])

    def __repr__(self):
         return '<Marqeta.response_models.business_card_holder_model.BusinessCardHolderModel>'