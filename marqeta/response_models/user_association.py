from datetime import datetime

class UserAssociation(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def single_inventory_user(self):
        if 'single_inventory_user' in self.json_response:
            return self.json_response['single_inventory_user']

    @property
    def single_inventory_user_token(self):
        if 'single_inventory_user_token' in self.json_response:
            return self.json_response['single_inventory_user_token']

