from marqeta.response_models.gl_entry import GlEntry

class GlTransactionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

