from datetime import datetime, date
import json

class DirectDepositTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'channel' : self.channel,
           'reason' : self.reason,
           'idempotentHash' : self.idempotentHash,
           'direct_deposit_token' : self.direct_deposit_token,
           'state' : self.state,
           'reason_code' : self.reason_code,
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

    def __repr__(self):
         return '<Marqeta.response_models.direct_deposit_transition_request.DirectDepositTransitionRequest>'