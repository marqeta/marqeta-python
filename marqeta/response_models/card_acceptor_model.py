from datetime import datetime, date
import json

class CardAcceptorModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'mcc' : self.mcc,
           'partial_approval_capable' : self.partial_approval_capable,
           'name' : self.name,
           'address' : self.address,
           'city' : self.city,
           'state' : self.state,
           'zip' : self.zip,
           'country' : self.country,
           'ecommerce_security_level_indicator' : self.ecommerce_security_level_indicator,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.card_acceptor_model.CardAcceptorModel>'