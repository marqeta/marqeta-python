from datetime import datetime

class CardInventoryRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def package_id(self):
        if 'package_id' in self.json_response:
            return self.json_response['package_id']

    @property
    def starting_inventory(self):
        if 'starting_inventory' in self.json_response:
            return self.json_response['starting_inventory']

