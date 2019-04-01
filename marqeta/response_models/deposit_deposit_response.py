from datetime import datetime, date
import json


class DepositDepositResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
            return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%d').date()

    @property
    def state_reason(self):
        return self.json_response.get('state_reason', None)

    @property
    def state_reason_code(self):
        return self.json_response.get('state_reason_code', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

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
        return self.json_response.get('standard_entry_class_code', None)

    @property
    def company_name(self):
        return self.json_response.get('company_name', None)

    @property
    def company_discretionary_data(self):
        return self.json_response.get('company_discretionary_data', None)

    @property
    def company_identification(self):
        return self.json_response.get('company_identification', None)

    @property
    def company_entry_description(self):
        return self.json_response.get('company_entry_description', None)

    @property
    def individual_identification_number(self):
        return self.json_response.get('individual_identification_number', None)

    @property
    def individual_name(self):
        return self.json_response.get('individual_name', None)

    def __repr__(self):
        return '<Marqeta.response_models.deposit_deposit_response.DepositDepositResponse>' + self.__str__()
