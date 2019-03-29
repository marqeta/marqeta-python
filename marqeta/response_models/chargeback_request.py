from datetime import datetime, date
import json


class ChargebackRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def transaction_token(self):
        return self.json_response.get('transaction_token', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def reason_description(self):
        return self.json_response.get('reason_description', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def memo(self):
        return self.json_response.get('memo', None)

    @property
    def credit_user(self):
        return self.json_response.get('credit_user', None)

    @property
    def channel(self):
        return self.json_response.get('channel', None)

    def __repr__(self):
        return '<Marqeta.response_models.chargeback_request.ChargebackRequest>'
