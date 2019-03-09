from datetime import datetime

class AchReturn(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def date(self):
        if 'date' in self.json_response:
            return datetime.strptime(self.json_response['date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def dateInitiated(self):
        if 'dateInitiated' in self.json_response:
            return datetime.strptime(self.json_response['dateInitiated'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def orderId(self):
        if 'orderId' in self.json_response:
            return self.json_response['orderId']

    @property
    def reasonCode(self):
        if 'reasonCode' in self.json_response:
            return self.json_response['reasonCode']

    @property
    def directDeposit(self):
        if 'directDeposit' in self.json_response:
            return self.json_response['directDeposit']

    @property
    def achType(self):
        if 'achType' in self.json_response:
            return self.json_response['achType']

