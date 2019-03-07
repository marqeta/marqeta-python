from datetime import datetime


class Fee(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']

    @property
    def amount(self):
        if 'amount' in self.response:
            return self.response['amount']

    @property
    def tags(self):
        if 'tags' in self.response:
            return self.response['tags']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def currency_code(self):
        if 'currency_code' in self.response:
            return self.response['currency_code']

    @property
    def real_time_assessment(self):
        if 'real_time_assessment' in self.response:
            return RealTimeFeeAssessment(self.response['real_time_assessment'])


class RealTimeFeeAssessment(object):

    def __init__(self, response):
        self.response = response

    @property
    def transaction_type(self):
        if 'transaction_type' in self.response:
            return self.response['transaction_type']

    @property
    def international_enabled(self):
        if 'international_enabled' in self.response:
            return self.response['international_enabled']

    @property
    def domestic_enabled(self):
        if 'domestic_enabled' in self.response:
            return self.response['domestic_enabled']
