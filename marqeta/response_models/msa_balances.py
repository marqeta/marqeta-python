from datetime import datetime, date
import json


class MsaBalances(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)

    @property
    def ledger_balance(self):
        return self.json_response.get('ledger_balance', None)

    @property
    def available_balance(self):
        return self.json_response.get('available_balance', None)

    @property
    def credit_balance(self):
        return self.json_response.get('credit_balance', None)

    @property
    def pending_credits(self):
        return self.json_response.get('pending_credits', None)

    @property
    def impacted_amount(self):
        return self.json_response.get('impacted_amount', None)

    @property
    def balances(self):
        return self.json_response.get('balances', None)

    def __repr__(self):
        return '<Marqeta.response_models.msa_balances.MsaBalances>' + self.__str__()
