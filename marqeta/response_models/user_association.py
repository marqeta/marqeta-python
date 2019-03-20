from datetime import datetime, date
import json

class UserAssociation(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def single_inventory_user(self):
        if 'single_inventory_user' in self.json_response:
            return self.json_response['single_inventory_user']

    @property
    def single_inventory_user_token(self):
        if 'single_inventory_user_token' in self.json_response:
            return self.json_response['single_inventory_user_token']

    def __repr__(self):
         return '<Marqeta.response_models.user_association.UserAssociation>'