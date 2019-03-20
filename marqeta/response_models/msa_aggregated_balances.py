from datetime import datetime, date
import json

class MsaAggregatedBalances(object):

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
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def ledger_balance(self):
        if 'ledger_balance' in self.json_response:
            return self.json_response['ledger_balance']

    @property
    def available_balance(self):
        if 'available_balance' in self.json_response:
            return self.json_response['available_balance']

    @property
    def credit_balance(self):
        if 'credit_balance' in self.json_response:
            return self.json_response['credit_balance']

    @property
    def pending_credits(self):
        if 'pending_credits' in self.json_response:
            return self.json_response['pending_credits']

    @property
    def impacted_amount(self):
        if 'impacted_amount' in self.json_response:
            return self.json_response['impacted_amount']

    @property
    def balances(self):
        if 'balances' in self.json_response:
            return self.json_response['balances']

    def __repr__(self):
         return '<Marqeta.response_models.msa_aggregated_balances.MsaAggregatedBalances>'