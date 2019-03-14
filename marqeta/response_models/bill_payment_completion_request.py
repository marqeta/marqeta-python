from datetime import datetime, date
import json

class BillPaymentCompletionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'network_reference_id' : self.network_reference_id,
           'original_transaction_token' : self.original_transaction_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def original_transaction_token(self):
        if 'original_transaction_token' in self.json_response:
            return self.json_response['original_transaction_token']

    def __repr__(self):
         return '<Marqeta.response_models.bill_payment_completion_request.BillPaymentCompletionRequest>'