from datetime import datetime, date
from marqeta.response_models.spend_control_association import SpendControlAssociation
from marqeta.response_models.merchant_scope import MerchantScope
import json


class VelocityControlResponse(object):

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
    def name(self):
        return self.json_response.get('name', None)

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
        return self.json_response.get('usage_limit', None)

    @property
    def approvals_only(self):
        return self.json_response.get('approvals_only', None)

    @property
    def include_purchases(self):
        return self.json_response.get('include_purchases', None)

    @property
    def include_withdrawals(self):
        return self.json_response.get('include_withdrawals', None)

    @property
    def include_transfers(self):
        return self.json_response.get('include_transfers', None)

    @property
    def include_cashback(self):
        return self.json_response.get('include_cashback', None)

    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)

    @property
    def amount_limit(self):
        return self.json_response.get('amount_limit', None)

    @property
    def velocity_window(self):
        return self.json_response.get('velocity_window', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    def __repr__(self):
        return '<Marqeta.response_models.velocity_control_response.VelocityControlResponse>' + self.__str__()
