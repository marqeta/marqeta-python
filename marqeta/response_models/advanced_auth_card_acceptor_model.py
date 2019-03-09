from datetime import datetime

class AdvancedAuthCardAcceptorModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def mcc(self):
        if 'mcc' in self.json_response:
            return self.json_response['mcc']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def address(self):
        if 'address' in self.json_response:
            return self.json_response['address']

    @property
    def city(self):
        if 'city' in self.json_response:
            return self.json_response['city']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def tid(self):
        if 'tid' in self.json_response:
            return self.json_response['tid']

