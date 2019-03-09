from datetime import datetime

class CardAcceptorModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def mcc(self):
        if 'mcc' in self.json_response:
            return self.json_response['mcc']

    @property
    def partial_approval_capable(self):
        if 'partial_approval_capable' in self.json_response:
            return self.json_response['partial_approval_capable']

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
    def ecommerce_security_level_indicator(self):
        if 'ecommerce_security_level_indicator' in self.json_response:
            return self.json_response['ecommerce_security_level_indicator']

