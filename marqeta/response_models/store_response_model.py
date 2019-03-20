from datetime import datetime, date
import json

class StoreResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def contact(self):
        if 'contact' in self.json_response:
            return self.json_response['contact']

    @property
    def contact_email(self):
        if 'contact_email' in self.json_response:
            return self.json_response['contact_email']

    @property
    def longitude(self):
        if 'longitude' in self.json_response:
            return self.json_response['longitude']

    @property
    def latitude(self):
        if 'latitude' in self.json_response:
            return self.json_response['latitude']

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
    def province(self):
        if 'province' in self.json_response:
            return self.json_response['province']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def partial_auth_flag(self):
        if 'partial_auth_flag' in self.json_response:
            return self.json_response['partial_auth_flag']

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def network_mid(self):
        if 'network_mid' in self.json_response:
            return self.json_response['network_mid']

    @property
    def merchant_token(self):
        if 'merchant_token' in self.json_response:
            return self.json_response['merchant_token']

    @property
    def partial_approval_capable(self):
        if 'partial_approval_capable' in self.json_response:
            return self.json_response['partial_approval_capable']

    @property
    def keyed_auth_cvv_enforced(self):
        if 'keyed_auth_cvv_enforced' in self.json_response:
            return self.json_response['keyed_auth_cvv_enforced']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
         return '<Marqeta.response_models.store_response_model.StoreResponseModel>'