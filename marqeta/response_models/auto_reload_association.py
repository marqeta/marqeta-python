from datetime import datetime, date
import json

class AutoReloadAssociation(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'card_product_token' : self.card_product_token,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_product_token(self):
        if 'card_product_token' in self.json_response:
            return self.json_response['card_product_token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    def __repr__(self):
         return '<Marqeta.response_models.auto_reload_association.AutoReloadAssociation>'