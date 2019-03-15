from datetime import datetime, date
from marqeta.response_models.spend_control_association import SpendControlAssociation
from marqeta.response_models.merchant_scope import MerchantScope
import json

class AuthControlResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'name' : self.name,
           'association' : self.association,
           'merchant_scope' : self.merchant_scope,
           'start_time' : self.start_time,
           'end_time' : self.end_time,
           'active' : self.active,
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
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def association(self):
        if 'association' in self.json_response:
            return SpendControlAssociation(self.json_response['association'])

    @property
    def merchant_scope(self):
        if 'merchant_scope' in self.json_response:
            return MerchantScope(self.json_response['merchant_scope'])

    @property
    def start_time(self):
        if 'start_time' in self.json_response:
                return datetime.strptime(self.json_response['start_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_time(self):
        if 'end_time' in self.json_response:
                return datetime.strptime(self.json_response['end_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    def __repr__(self):
         return '<Marqeta.response_models.auth_control_response.AuthControlResponse>'