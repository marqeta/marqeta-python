from datetime import datetime, date
import json

class DirectDepositRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'amount' : self.amount,
           'type' : self.type,
           'account_number' : self.account_number,
           'settlement_date' : self.settlement_date,
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
    def account_number(self):
        if 'account_number' in self.json_response:
            return self.json_response['account_number']

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
                return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%d').date()

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
         return '<Marqeta.response_models.direct_deposit_request.DirectDepositRequest>'