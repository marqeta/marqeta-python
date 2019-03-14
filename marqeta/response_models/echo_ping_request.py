from datetime import datetime, date
import json

class EchoPingRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'payload' : self.payload,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def payload(self):
        if 'payload' in self.json_response:
            return self.json_response['payload']

    def __repr__(self):
         return '<Marqeta.response_models.echo_ping_request.EchoPingRequest>'