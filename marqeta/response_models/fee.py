from datetime import datetime


class Fee(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def real_time_assessment(self):
        if 'real_time_assessment' in self.json_response:
            return RealTimeFeeAssessment(self.json_response['real_time_assessment'])


class RealTimeFeeAssessment(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def transaction_type(self):
        if 'transaction_type' in self.json_response:
            return self.json_response['transaction_type']

    @property
    def international_enabled(self):
        if 'international_enabled' in self.json_response:
            return self.json_response['international_enabled']

    @property
    def domestic_enabled(self):
        if 'domestic_enabled' in self.json_response:
            return self.json_response['domestic_enabled']
