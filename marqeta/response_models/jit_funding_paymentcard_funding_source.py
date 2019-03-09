from datetime import datetime

class JitFundingPaymentcardFundingSource(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def enabled(self):
        if 'enabled' in self.json_response:
            return self.json_response['enabled']

    @property
    def refunds_destination(self):
        if 'refunds_destination' in self.json_response:
            return self.json_response['refunds_destination']

