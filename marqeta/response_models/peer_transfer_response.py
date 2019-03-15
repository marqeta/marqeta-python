from datetime import datetime, date
import json

class PeerTransferResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'amount' : self.amount,
           'tags' : self.tags,
           'memo' : self.memo,
           'currency_code' : self.currency_code,
           'sender_user_token' : self.sender_user_token,
           'recipient_user_token' : self.recipient_user_token,
           'sender_business_token' : self.sender_business_token,
           'recipient_business_token' : self.recipient_business_token,
           'created_time' : self.created_time,
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
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

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
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
         return '<Marqeta.response_models.peer_transfer_response.PeerTransferResponse>'