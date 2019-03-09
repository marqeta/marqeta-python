from datetime import datetime

class DirectDepositTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def idempotentHash(self):
        if 'idempotentHash' in self.json_response:
            return self.json_response['idempotentHash']

    @property
    def direct_deposit_token(self):
        if 'direct_deposit_token' in self.json_response:
            return self.json_response['direct_deposit_token']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

