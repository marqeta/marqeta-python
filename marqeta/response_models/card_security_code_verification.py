from datetime import datetime
from marqeta.response_models.response import Response

class CardSecurityCodeVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

