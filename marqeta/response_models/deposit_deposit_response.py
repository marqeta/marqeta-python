from datetime import datetime

class DepositDepositResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
            return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def state_reason(self):
        if 'state_reason' in self.json_response:
            return self.json_response['state_reason']

    @property
    def state_reason_code(self):
        if 'state_reason_code' in self.json_response:
            return self.json_response['state_reason_code']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def standard_entry_class_code(self):
        if 'standard_entry_class_code' in self.json_response:
            return self.json_response['standard_entry_class_code']

    @property
    def company_name(self):
        if 'company_name' in self.json_response:
            return self.json_response['company_name']

    @property
    def company_discretionary_data(self):
        if 'company_discretionary_data' in self.json_response:
            return self.json_response['company_discretionary_data']

    @property
    def company_identification(self):
        if 'company_identification' in self.json_response:
            return self.json_response['company_identification']

    @property
    def company_entry_description(self):
        if 'company_entry_description' in self.json_response:
            return self.json_response['company_entry_description']

    @property
    def individual_identification_number(self):
        if 'individual_identification_number' in self.json_response:
            return self.json_response['individual_identification_number']

    @property
    def individual_name(self):
        if 'individual_name' in self.json_response:
            return self.json_response['individual_name']

