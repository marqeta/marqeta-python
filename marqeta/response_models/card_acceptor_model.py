from datetime import datetime, date
import json


class CardAcceptorModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def mcc(self):
        return self.json_response.get('mcc', None)

    @property
    def partial_approval_capable(self):
        return self.json_response.get('partial_approval_capable', None)

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
    def ecommerce_security_level_indicator(self):
        return self.json_response.get('ecommerce_security_level_indicator', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_acceptor_model.CardAcceptorModel>'
