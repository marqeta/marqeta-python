from datetime import datetime
from marqeta.response_models.terminal_model import TerminalModel

class TransactionCardAcceptorViewModelV1(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def mcc(self):
        if 'mcc' in self.json_response:
            return self.json_response['mcc']

    @property
    def network_mid(self):
        if 'network_mid' in self.json_response:
            return self.json_response['network_mid']

    @property
    def mcc_groups(self):
        if 'mcc_groups' in self.json_response:
            return self.json_response['mcc_groups']

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
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def poi(self):
        if 'poi' in self.json_response:
            return TerminalModel(self.json_response['poi'])

