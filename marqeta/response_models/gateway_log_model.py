from datetime import datetime, date
from marqeta.response_models.gateway_response import GatewayResponse
import json

class GatewayLogModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'order_number' : self.order_number,
           'transaction_id' : self.transaction_id,
           'message' : self.message,
           'duration' : self.duration,
           'timed_out' : self.timed_out,
           'response' : self.response,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def order_number(self):
        if 'order_number' in self.json_response:
            return self.json_response['order_number']

    @property
    def transaction_id(self):
        if 'transaction_id' in self.json_response:
            return self.json_response['transaction_id']

    @property
    def message(self):
        if 'message' in self.json_response:
            return self.json_response['message']

    @property
    def duration(self):
        if 'duration' in self.json_response:
            return self.json_response['duration']

    @property
    def timed_out(self):
        if 'timed_out' in self.json_response:
            return self.json_response['timed_out']

    @property
    def response(self):
        if 'response' in self.json_response:
            return GatewayResponse(self.json_response['response'])

    def __repr__(self):
         return '<Marqeta.response_models.gateway_log_model.GatewayLogModel>'