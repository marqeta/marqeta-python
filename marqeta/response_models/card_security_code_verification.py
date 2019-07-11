from datetime import datetime, date
from marqeta.response_models.response import Response
from marqeta.response_models import datetime_object
import json
import re

class CardSecurityCodeVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        return self.json_response.get('type', None)


    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

    def __repr__(self):
         return '<Marqeta.response_models.card_security_code_verification.CardSecurityCodeVerification>' + self.__str__()
