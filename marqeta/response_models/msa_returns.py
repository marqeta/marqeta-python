from datetime import datetime, date
from marqeta.response_models.msa_balances import MsaBalances
from marqeta.response_models.funding import Funding
from marqeta.response_models.msa_aggregated_balances import MsaAggregatedBalances
import json


class MsaReturns(object):

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
    def user_token(self):

        return self.json_response.get('user_token', None)

    @property
    def business_token(self):

        return self.json_response.get('business_token', None)

    @property
    def order_balances(self):

        if 'order_balances' in self.json_response:
            return MsaBalances(self.json_response['order_balances'])

    @property
    def amount(self):

        return self.json_response.get('amount', None)

    @property
    def last_transaction_date(self):

        if 'last_transaction_date' in self.json_response:
            return datetime.strptime(self.json_response['last_transaction_date'], '%Y-%m-%d').date()

    @property
    def start_date(self):

        if 'start_date' in self.json_response:
            return datetime.strptime(self.json_response['start_date'], '%Y-%m-%d').date()

    @property
    def end_date(self):

        if 'end_date' in self.json_response:
            return datetime.strptime(self.json_response['end_date'], '%Y-%m-%d').date()

    @property
    def currency_code(self):

        return self.json_response.get('currency_code', None)

    @property
    def active(self):

        return self.json_response.get('active', None)

    @property
    def reward_amount(self):

        return self.json_response.get('reward_amount', None)

    @property
    def reward_trigger_amount(self):

        return self.json_response.get('reward_trigger_amount', None)

    @property
    def unloaded_amount(self):

        return self.json_response.get('unloaded_amount', None)

    @property
    def campaign_token(self):

        return self.json_response.get('campaign_token', None)

    @property
    def funding(self):

        if 'funding' in self.json_response:
            return Funding(self.json_response['funding'])

    @property
    def created_time(self):

        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):

        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def aggregated_balances(self):

        if 'aggregated_balances' in self.json_response:
            return MsaAggregatedBalances(self.json_response['aggregated_balances'])

    @property
    def original_order_token(self):

        return self.json_response.get('original_order_token', None)

    @property
    def transaction_token(self):

        return self.json_response.get('transaction_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.msa_returns.MsaReturns>'
