from datetime import datetime, date
import json


class DirectDepositTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def channel(self):
        return self.json_response.get('channel', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def reason(self):
        return self.json_response.get('reason', None)

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def direct_deposit_token(self):
        return self.json_response.get('direct_deposit_token', None)

    @property
    def transaction_token(self):
        return self.json_response.get('transaction_token', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.direct_deposit_transition_response.DirectDepositTransitionResponse>'
