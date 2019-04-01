from datetime import datetime, date
from marqeta.response_models.avs_controls import AvsControls
import json


class TransactionControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def accepted_countries_token(self):
        return self.json_response.get('accepted_countries_token', None)

    @property
    def always_require_pin(self):
        return self.json_response.get('always_require_pin', None)

    @property
    def always_require_icc(self):
        return self.json_response.get('always_require_icc', None)

    @property
    def allow_gpa_auth(self):
        return self.json_response.get('allow_gpa_auth', None)

    @property
    def require_card_not_present_card_security_code(self):
        return self.json_response.get('require_card_not_present_card_security_code', None)

    @property
    def allow_mcc_group_authorization_controls(self):
        return self.json_response.get('allow_mcc_group_authorization_controls', None)

    @property
    def allow_first_pin_set_via_financial_transaction(self):
        return self.json_response.get('allow_first_pin_set_via_financial_transaction', None)

    @property
    def ignore_card_suspended_state(self):
        return self.json_response.get('ignore_card_suspended_state', None)

    @property
    def allow_network_load(self):
        return self.json_response.get('allow_network_load', None)

    @property
    def allow_network_load_card_activation(self):
        return self.json_response.get('allow_network_load_card_activation', None)

    @property
    def allow_quasi_cash(self):
        return self.json_response.get('allow_quasi_cash', None)

    @property
    def enable_partial_auth_approval(self):
        return self.json_response.get('enable_partial_auth_approval', None)

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return AvsControls(self.json_response['address_verification'])

    def __repr__(self):
        return '<Marqeta.response_models.transaction_controls.TransactionControls>'
