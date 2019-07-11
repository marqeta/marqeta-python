from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class PreKycControls(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def cash_access_enabled(self):
        return self.json_response.get('cash_access_enabled', None)

    @property
    def international_enabled(self):
        return self.json_response.get('international_enabled', None)

    @property
    def balance_max(self):
        return self.json_response.get('balance_max', None)

    @property
    def enable_non_program_loads(self):
        return self.json_response.get('enable_non_program_loads', None)

    @property
    def is_reloadable_pre_kyc(self):
        return self.json_response.get('is_reloadable_pre_kyc', None)

    def __repr__(self):
         return '<Marqeta.response_models.pre_kyc_controls.PreKycControls>' + self.__str__()
