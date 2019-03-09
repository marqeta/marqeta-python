from datetime import datetime
from marqeta.response_models.pre_kyc_controls import PreKycControls

class AccountHolderGroupConfig(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def kyc_required(self):
        if 'kyc_required' in self.json_response:
            return self.json_response['kyc_required']

    @property
    def is_reloadable(self):
        if 'is_reloadable' in self.json_response:
            return self.json_response['is_reloadable']

    @property
    def real_time_fee_group_token(self):
        if 'real_time_fee_group_token' in self.json_response:
            return self.json_response['real_time_fee_group_token']

    @property
    def pre_kyc_controls(self):
        if 'pre_kyc_controls' in self.json_response:
            return PreKycControls(self.json_response['pre_kyc_controls'])

