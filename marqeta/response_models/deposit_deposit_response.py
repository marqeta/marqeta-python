from datetime import datetime, date
import json

class DepositDepositResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'amount' : self.amount,
           'type' : self.type,
           'state' : self.state,
           'settlement_date' : self.settlement_date,
           'state_reason' : self.state_reason,
           'state_reason_code' : self.state_reason_code,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'standard_entry_class_code' : self.standard_entry_class_code,
           'company_name' : self.company_name,
           'company_discretionary_data' : self.company_discretionary_data,
           'company_identification' : self.company_identification,
           'company_entry_description' : self.company_entry_description,
           'individual_identification_number' : self.individual_identification_number,
           'individual_name' : self.individual_name,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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
                return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%d').date()

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

    def __repr__(self):
         return '<Marqeta.response_models.deposit_deposit_response.DepositDepositResponse>'