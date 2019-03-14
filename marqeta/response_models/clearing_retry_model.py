from datetime import datetime, date
import json

class ClearingRetryModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'original_failed_transaction_token' : self.original_failed_transaction_token,
           'new_network_reference' : self.new_network_reference,
           'new_approval_code' : self.new_approval_code,
           'new_stan' : self.new_stan,
           'find_original_window_days' : self.find_original_window_days,
           'new_processing_code' : self.new_processing_code,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def original_failed_transaction_token(self):
        if 'original_failed_transaction_token' in self.json_response:
            return self.json_response['original_failed_transaction_token']

    @property
    def new_network_reference(self):
        if 'new_network_reference' in self.json_response:
            return self.json_response['new_network_reference']

    @property
    def new_approval_code(self):
        if 'new_approval_code' in self.json_response:
            return self.json_response['new_approval_code']

    @property
    def new_stan(self):
        if 'new_stan' in self.json_response:
            return self.json_response['new_stan']

    @property
    def find_original_window_days(self):
        if 'find_original_window_days' in self.json_response:
            return self.json_response['find_original_window_days']

    @property
    def new_processing_code(self):
        if 'new_processing_code' in self.json_response:
            return self.json_response['new_processing_code']

    def __repr__(self):
         return '<Marqeta.response_models.clearing_retry_model.ClearingRetryModel>'