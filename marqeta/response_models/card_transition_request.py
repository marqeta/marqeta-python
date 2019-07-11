from datetime import datetime, date
from marqeta.response_models.validations_request import ValidationsRequest
from marqeta.response_models import datetime_object
import json
import re

class CardTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def card_token(self):
        return self.json_response.get('card_token', None)


    @property
    def reason(self):
        return self.json_response.get('reason', None)


    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)


    @property
    def validations(self):
        if 'validations' in self.json_response:
            return ValidationsRequest(self.json_response['validations'])

    @property
    def channel(self):
        return self.json_response.get('channel', None)


    @property
    def state(self):
        return self.json_response.get('state', None)


    def __repr__(self):
         return '<Marqeta.response_models.card_transition_request.CardTransitionRequest>' + self.__str__()
