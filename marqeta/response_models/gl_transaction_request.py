from datetime import datetime, date
from marqeta.response_models.gl_entry import GlEntry
import json

class GlTransactionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def entries(self):
        if 'entries' in self.json_response:
            return [GlEntry(val) for val in self.json_response['entries']]

    @property
    def detail(self):
        if 'detail' in self.json_response:
            return self.json_response['detail']

    @property
    def cardholder_visible(self):
        if 'cardholder_visible' in self.json_response:
            return self.json_response['cardholder_visible']

    @property
    def reference_transaction_token(self):
        if 'reference_transaction_token' in self.json_response:
            return self.json_response['reference_transaction_token']

    def __repr__(self):
         return '<Marqeta.response_models.gl_transaction_request.GlTransactionRequest>'