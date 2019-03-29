from datetime import datetime, date
import json


class ReplacementAmount(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_amount(self):
        return self.json_response.get('transaction_amount', None)

    @property
    def settlement_amount(self):
        return self.json_response.get('settlement_amount', None)

    @property
    def transaction_fee(self):
        return self.json_response.get('transaction_fee', None)

    @property
    def settlement_fee(self):
        return self.json_response.get('settlement_fee', None)

    def __repr__(self):
        return '<Marqeta.response_models.replacement_amount.ReplacementAmount>'
