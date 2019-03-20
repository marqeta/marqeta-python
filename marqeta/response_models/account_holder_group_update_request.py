from datetime import datetime, date
from marqeta.response_models.account_holder_group_config import AccountHolderGroupConfig
import json

class AccountHolderGroupUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def config(self):
        if 'config' in self.json_response:
            return AccountHolderGroupConfig(self.json_response['config'])

    def __repr__(self):
         return '<Marqeta.response_models.account_holder_group_update_request.AccountHolderGroupUpdateRequest>'