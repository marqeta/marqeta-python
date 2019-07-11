from datetime import datetime, date
from marqeta.response_models.expiration_offset import ExpirationOffset
from marqeta.response_models import datetime_object
import json
import re

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
        return self.json_response.get('activate_upon_issue', None)

    @property
    def expiration_offset(self):
        if 'expiration_offset' in self.json_response:
            return ExpirationOffset(self.json_response['expiration_offset'])

    @property
    def card_service_code(self):
        return self.json_response.get('card_service_code', None)

    @property
    def update_expiration_upon_activation(self):
        return self.json_response.get('update_expiration_upon_activation', None)

    def __repr__(self):
         return '<Marqeta.response_models.card_life_cycle.CardLifeCycle>' + self.__str__()
