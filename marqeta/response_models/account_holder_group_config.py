from datetime import datetime, date
from marqeta.response_models.pre_kyc_controls import PreKycControls
import json


class AccountHolderGroupConfig(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def kyc_required(self):
        return self.json_response.get('kyc_required', None)

    @property
    def is_reloadable(self):
        return self.json_response.get('is_reloadable', None)

    @property
    def real_time_fee_group_token(self):
        return self.json_response.get('real_time_fee_group_token', None)

    @property
    def pre_kyc_controls(self):
        if 'pre_kyc_controls' in self.json_response:
            return PreKycControls(self.json_response['pre_kyc_controls'])

    def __repr__(self):
        return '<Marqeta.response_models.account_holder_group_config.AccountHolderGroupConfig>' + self.__str__()
