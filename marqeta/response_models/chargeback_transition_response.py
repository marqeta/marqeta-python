from datetime import datetime, date
import json

class ChargebackTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'state' : self.state,
           'previous_state' : self.previous_state,
           'channel' : self.channel,
           'chargeback_token' : self.chargeback_token,
           'reason' : self.reason,
           'transaction_token' : self.transaction_token,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'type' : self.type,
           'amount' : self.amount,
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
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def previous_state(self):
        if 'previous_state' in self.json_response:
            return self.json_response['previous_state']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def chargeback_token(self):
        if 'chargeback_token' in self.json_response:
            return self.json_response['chargeback_token']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    def __repr__(self):
         return '<Marqeta.response_models.chargeback_transition_response.ChargebackTransitionResponse>'