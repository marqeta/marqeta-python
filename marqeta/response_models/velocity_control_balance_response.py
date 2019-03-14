from datetime import datetime, date
from marqeta.response_models.spend_control_association import SpendControlAssociation
from marqeta.response_models.merchant_scope import MerchantScope
from marqeta.response_models.available import Available
import json

class VelocityControlBalanceResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'name' : self.name,
           'association' : self.association,
           'merchant_scope' : self.merchant_scope,
           'usage_limit' : self.usage_limit,
           'approvals_only' : self.approvals_only,
           'include_purchases' : self.include_purchases,
           'include_withdrawals' : self.include_withdrawals,
           'include_transfers' : self.include_transfers,
           'include_cashback' : self.include_cashback,
           'currency_code' : self.currency_code,
           'amount_limit' : self.amount_limit,
           'velocity_window' : self.velocity_window,
           'active' : self.active,
           'available' : self.available,
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
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def association(self):
        if 'association' in self.json_response:
            return SpendControlAssociation(self.json_response['association'])

    @property
    def merchant_scope(self):
        if 'merchant_scope' in self.json_response:
            return MerchantScope(self.json_response['merchant_scope'])

    @property
    def usage_limit(self):
        if 'usage_limit' in self.json_response:
            return self.json_response['usage_limit']

    @property
    def approvals_only(self):
        if 'approvals_only' in self.json_response:
            return self.json_response['approvals_only']

    @property
    def include_purchases(self):
        if 'include_purchases' in self.json_response:
            return self.json_response['include_purchases']

    @property
    def include_withdrawals(self):
        if 'include_withdrawals' in self.json_response:
            return self.json_response['include_withdrawals']

    @property
    def include_transfers(self):
        if 'include_transfers' in self.json_response:
            return self.json_response['include_transfers']

    @property
    def include_cashback(self):
        if 'include_cashback' in self.json_response:
            return self.json_response['include_cashback']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def amount_limit(self):
        if 'amount_limit' in self.json_response:
            return self.json_response['amount_limit']

    @property
    def velocity_window(self):
        if 'velocity_window' in self.json_response:
            return self.json_response['velocity_window']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def available(self):
        if 'available' in self.json_response:
            return Available(self.json_response['available'])

    def __repr__(self):
         return '<Marqeta.response_models.velocity_control_balance_response.VelocityControlBalanceResponse>'