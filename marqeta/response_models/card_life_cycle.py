from datetime import datetime, date
from marqeta.response_models.expiration_offset import ExpirationOffset
import json

class CardLifeCycle(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def activate_upon_issue(self):
        if 'activate_upon_issue' in self.json_response:
            return self.json_response['activate_upon_issue']

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffset(self.json_response['expiration_offset'])

    @property
    def card_service_code(self):
        if 'card_service_code' in self.json_response:
            return self.json_response['card_service_code']

    @property
    def update_expiration_upon_activation(self):
        if 'update_expiration_upon_activation' in self.json_response:
            return self.json_response['update_expiration_upon_activation']

    def __repr__(self):
         return '<Marqeta.response_models.card_life_cycle.CardLifeCycle>'