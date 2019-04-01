from datetime import datetime, date
import json


class FundingAccountResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def account_suffix(self):
        return self.json_response.get('account_suffix', None)

    @property
    def account_type(self):
        return self.json_response.get('account_type', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def is_default_account(self):
        return self.json_response.get('is_default_account', None)

    @property
    def exp_date(self):
        return self.json_response.get('exp_date', None)

    @property
    def verification_status(self):
        return self.json_response.get('verification_status', None)

    @property
    def date_verified(self):
        if 'date_verified' in self.json_response:
            return datetime.strptime(self.json_response['date_verified'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def name_on_account(self):
        return self.json_response.get('name_on_account', None)

    @property
    def date_sent_for_verification(self):
        if 'date_sent_for_verification' in self.json_response:
            return datetime.strptime(self.json_response['date_sent_for_verification'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def verification_override(self):
        return self.json_response.get('verification_override', None)

    @property
    def verification_notes(self):
        return self.json_response.get('verification_notes', None)

    def __repr__(self):
        return '<Marqeta.response_models.funding_account_response_model.FundingAccountResponseModel>' + self.__str__()
