from datetime import datetime

class PeerTransferRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    @property
    def sender_user_token(self):
        if 'sender_user_token' in self.json_response:
            return self.json_response['sender_user_token']

    @property
    def recipient_user_token(self):
        if 'recipient_user_token' in self.json_response:
            return self.json_response['recipient_user_token']

    @property
    def sender_business_token(self):
        if 'sender_business_token' in self.json_response:
            return self.json_response['sender_business_token']

    @property
    def recipient_business_token(self):
        if 'recipient_business_token' in self.json_response:
            return self.json_response['recipient_business_token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

