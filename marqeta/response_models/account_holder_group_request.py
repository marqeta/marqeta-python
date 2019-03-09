from datetime import datetime
from marqeta.response_models.account_holder_group_config import AccountHolderGroupConfig

class AccountHolderGroupRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def config(self):
        if 'config' in self.json_response:
            return AccountHolderGroupConfig(self.json_response['config'])

