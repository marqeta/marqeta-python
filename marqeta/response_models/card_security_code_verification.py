from datetime import datetime, date
from marqeta.response_models.response import Response
import json

class CardSecurityCodeVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'type' : self.type,
           'response' : self.response,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

    def __repr__(self):
         return '<Marqeta.response_models.card_security_code_verification.CardSecurityCodeVerification>'