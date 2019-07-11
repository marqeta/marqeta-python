from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class TerminalModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def tid(self):
        return self.json_response.get('tid', None)


    @property
    def partial_approval_capable(self):
        return self.json_response.get('partial_approval_capable', None)


    @property
    def cardholder_presence(self):
        return self.json_response.get('cardholder_presence', None)


    @property
    def card_presence(self):
        return self.json_response.get('card_presence', None)


    @property
    def channel(self):
        return self.json_response.get('channel', None)


    @property
    def processing_type(self):
        return self.json_response.get('processing_type', None)


    @property
    def pin_present(self):
        return self.json_response.get('pin_present', None)


    def __repr__(self):
         return '<Marqeta.response_models.terminal_model.TerminalModel>' + self.__str__()
