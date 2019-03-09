from datetime import datetime
from marqeta.response_models.spend_control_association import SpendControlAssociation
from marqeta.response_models.merchant_scope import MerchantScope

class VelocityControlUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

