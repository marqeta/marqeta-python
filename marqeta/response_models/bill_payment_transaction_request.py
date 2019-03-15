from datetime import datetime, date
import json

class BillPaymentTransactionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'amount' : self.amount,
           'currency' : self.currency,
           'network_reference_id' : self.network_reference_id,
           'user_token' : self.user_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def currency(self):
        if 'currency' in self.json_response:
            return self.json_response['currency']

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    def __repr__(self):
         return '<Marqeta.response_models.bill_payment_transaction_request.BillPaymentTransactionRequest>'