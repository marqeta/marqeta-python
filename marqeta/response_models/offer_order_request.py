from datetime import datetime, date
import json

class OfferOrderRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'offer_token' : self.offer_token,
           'funding_source_token' : self.funding_source_token,
           'funding_source_address_token' : self.funding_source_address_token,
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
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def offer_token(self):
        if 'offer_token' in self.json_response:
            return self.json_response['offer_token']

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.json_response:
            return self.json_response['funding_source_token']

    @property
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.json_response:
            return self.json_response['funding_source_address_token']

    def __repr__(self):
         return '<Marqeta.response_models.offer_order_request.OfferOrderRequest>'