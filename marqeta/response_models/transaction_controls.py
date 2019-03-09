from datetime import datetime
from marqeta.response_models.avs_controls import AvsControls

class TransactionControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def accepted_countries_token(self):
        if 'accepted_countries_token' in self.json_response:
            return self.json_response['accepted_countries_token']

    @property
    def always_require_pin(self):
        if 'always_require_pin' in self.json_response:
            return self.json_response['always_require_pin']

    @property
    def always_require_icc(self):
        if 'always_require_icc' in self.json_response:
            return self.json_response['always_require_icc']

    @property
    def allow_gpa_auth(self):
        if 'allow_gpa_auth' in self.json_response:
            return self.json_response['allow_gpa_auth']

    @property
    def require_card_not_present_card_security_code(self):
        if 'require_card_not_present_card_security_code' in self.json_response:
            return self.json_response['require_card_not_present_card_security_code']

    @property
    def allow_mcc_group_authorization_controls(self):
        if 'allow_mcc_group_authorization_controls' in self.json_response:
            return self.json_response['allow_mcc_group_authorization_controls']

    @property
    def allow_first_pin_set_via_financial_transaction(self):
        if 'allow_first_pin_set_via_financial_transaction' in self.json_response:
            return self.json_response['allow_first_pin_set_via_financial_transaction']

    @property
    def ignore_card_suspended_state(self):
        if 'ignore_card_suspended_state' in self.json_response:
            return self.json_response['ignore_card_suspended_state']

    @property
    def allow_network_load(self):
        if 'allow_network_load' in self.json_response:
            return self.json_response['allow_network_load']

    @property
    def allow_network_load_card_activation(self):
        if 'allow_network_load_card_activation' in self.json_response:
            return self.json_response['allow_network_load_card_activation']

    @property
    def allow_quasi_cash(self):
        if 'allow_quasi_cash' in self.json_response:
            return self.json_response['allow_quasi_cash']

    @property
    def enable_partial_auth_approval(self):
        if 'enable_partial_auth_approval' in self.json_response:
            return self.json_response['enable_partial_auth_approval']

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return AvsControls(self.json_response['address_verification'])

