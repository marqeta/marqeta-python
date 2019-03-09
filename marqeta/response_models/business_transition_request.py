from datetime import datetime

class BusinessTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def idempotentHash(self):
        if 'idempotentHash' in self.json_response:
            return self.json_response['idempotentHash']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

