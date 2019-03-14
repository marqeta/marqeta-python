from datetime import datetime, date
from marqeta.response_models.pre_kyc_controls import PreKycControls
import json

class AccountHolderGroupConfig(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'kyc_required' : self.kyc_required,
           'is_reloadable' : self.is_reloadable,
           'real_time_fee_group_token' : self.real_time_fee_group_token,
           'pre_kyc_controls' : self.pre_kyc_controls,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.account_holder_group_config.AccountHolderGroupConfig>'