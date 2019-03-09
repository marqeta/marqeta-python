from datetime import datetime
from marqeta.response_models.jit_funding_api import JitFundingApi

class JitProgramResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def jit_funding(self):
        if 'jit_funding' in self.json_response:
            return JitFundingApi(self.json_response['jit_funding'])

