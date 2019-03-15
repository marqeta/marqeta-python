from datetime import datetime, date
import json

class ChargebackTransitionRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'state' : self.state,
           'chargeback_token' : self.chargeback_token,
           'reason' : self.reason,
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
    def chargeback_token(self):
        if 'chargeback_token' in self.json_response:
            return self.json_response['chargeback_token']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    def __repr__(self):
         return '<Marqeta.response_models.chargeback_transition_request.ChargebackTransitionRequest>'