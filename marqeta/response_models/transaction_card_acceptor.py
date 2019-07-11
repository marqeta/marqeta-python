from datetime import datetime, date
from marqeta.response_models.terminal_model import TerminalModel
from marqeta.response_models import datetime_object
import json
import re

class TransactionCardAcceptor(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def mid(self):
        return self.json_response.get('mid', None)


    @property
    def mcc(self):
        return self.json_response.get('mcc', None)


    @property
    def network_mid(self):
        return self.json_response.get('network_mid', None)


    @property
    def mcc_groups(self):
        return self.json_response.get('mcc_groups', None)

    @property
    def name(self):
        return self.json_response.get('name', None)


    @property
    def address(self):
        return self.json_response.get('address', None)


    @property
    def city(self):
        return self.json_response.get('city', None)


    @property
    def state(self):
        return self.json_response.get('state', None)


    @property
    def zip(self):
        return self.json_response.get('zip', None)


    @property
    def country(self):
        return self.json_response.get('country', None)


    @property
    def poi(self):
        if 'poi' in self.json_response:
            return TerminalModel(self.json_response['poi'])

    def __repr__(self):
         return '<Marqeta.response_models.transaction_card_acceptor.TransactionCardAcceptor>' + self.__str__()
