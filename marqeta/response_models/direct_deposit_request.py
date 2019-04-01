from datetime import datetime, date
import json


class DirectDepositRequest(object):

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
    def account_number(self):
        return self.json_response.get('account_number', None)

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
            return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%d').date()

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
        return '<Marqeta.response_models.direct_deposit_request.DirectDepositRequest>'
