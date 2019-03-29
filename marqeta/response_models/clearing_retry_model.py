from datetime import datetime, date
import json


class ClearingRetryModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def original_failed_transaction_token(self):
        return self.json_response.get('original_failed_transaction_token', None)

    @property
    def new_network_reference(self):
        return self.json_response.get('new_network_reference', None)

    @property
    def new_approval_code(self):
        return self.json_response.get('new_approval_code', None)

    @property
    def new_stan(self):
        return self.json_response.get('new_stan', None)

    @property
    def find_original_window_days(self):
        return self.json_response.get('find_original_window_days', None)

    @property
    def new_processing_code(self):
        return self.json_response.get('new_processing_code', None)

    def __repr__(self):
        return '<Marqeta.response_models.clearing_retry_model.ClearingRetryModel>'
