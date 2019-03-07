from datetime import datetime


class AchResponseModel(object):

    def __init__(self, response):
        self.response = response

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def account_suffix(self):
        if 'account_suffix' in self.response:
            return self.response['account_suffix']

    @property
    def verification_status(self):
        if 'verification_status' in self.response:
            return self.response['verification_status']

    @property
    def account_type(self):
        if 'account_type' in self.response:
            return self.response['account_type']

    @property
    def name_on_account(self):
        if 'name_on_account' in self.response:
            return self.response['name_on_account']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def date_sent_for_verification(self):
        if 'date_sent_for_verification' in self.response:
            return datetime.strptime(self.response['date_sent_for_verification'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.response:
            return self.response['business_token']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.response:
            return self.response['is_default_account']

    @property
    def date_verified(self):
        if 'date_verified' in self.response:
            return datetime.strptime(self.response['date_verified'], '%Y-%m-%dT%H:%M:%SZ').date()

    @property
    def verification_override(self):
        if 'verification_override' in self.response:
            return self.response['verification_override']

    @property
    def verification_notes(self):
        if 'verification_notes' in self.response:
            return self.response['verification_notes']
