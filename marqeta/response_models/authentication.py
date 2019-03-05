"""Authentication Model with Authentication Properties!!!"""

from datetime import datetime


class Authentication(object):

    def __init__(self, response):
        self.response = response

    @property
    def last_password_update_channel(self):
        if 'last_password_update_channel' in self.response:
            return self.response['last_password_update_channel']

    @property
    def last_password_update_time(self):
        if 'last_password_update_time' in self.response:
            return datetime.strptime(self.response['last_password_update_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def email_verified(self):
        if 'email_verified' in self.response:
            return self.response['email_verified']

    @property
    def email_verified_time(self):
        if 'email_verified_time' in self.response:
            return datetime.strptime(self.response['email_verified_time'], '%Y-%m-%dT%H:%M:%SZ')
