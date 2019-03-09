from datetime import datetime

class DirectDepositTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def direct_deposit_token(self):
        if 'direct_deposit_token' in self.json_response:
            return self.json_response['direct_deposit_token']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

