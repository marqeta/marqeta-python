from datetime import datetime, date
import json

class DirectDepositTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'channel' : self.channel,
           'token' : self.token,
           'reason' : self.reason,
           'type' : self.type,
           'direct_deposit_token' : self.direct_deposit_token,
           'transaction_token' : self.transaction_token,
           'state' : self.state,
           'reason_code' : self.reason_code,
           'created_time' : self.created_time,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.direct_deposit_transition_response.DirectDepositTransitionResponse>'