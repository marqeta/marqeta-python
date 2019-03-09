from datetime import datetime

class PreKycControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def cash_access_enabled(self):
        if 'cash_access_enabled' in self.json_response:
            return self.json_response['cash_access_enabled']

    @property
    def international_enabled(self):
        if 'international_enabled' in self.json_response:
            return self.json_response['international_enabled']

    @property
    def balance_max(self):
        if 'balance_max' in self.json_response:
            return self.json_response['balance_max']

    @property
    def enable_non_program_loads(self):
        if 'enable_non_program_loads' in self.json_response:
            return self.json_response['enable_non_program_loads']

    @property
    def is_reloadable_pre_kyc(self):
        if 'is_reloadable_pre_kyc' in self.json_response:
            return self.json_response['is_reloadable_pre_kyc']

