from datetime import datetime

class JitFundingProgramFundingSource(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def enabled(self):
        if 'enabled' in self.json_response:
            return self.json_response['enabled']

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.json_response:
            return self.json_response['funding_source_token']

    @property
    def refunds_destination(self):
        if 'refunds_destination' in self.json_response:
            return self.json_response['refunds_destination']

