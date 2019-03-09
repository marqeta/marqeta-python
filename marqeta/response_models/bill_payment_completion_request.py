from datetime import datetime

class BillPaymentCompletionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def original_transaction_token(self):
        if 'original_transaction_token' in self.json_response:
            return self.json_response['original_transaction_token']

