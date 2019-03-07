"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime


class PanResponse(object):

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
    def user_token(self):
        if 'user_token' in self.response:
            return self.response['user_token']

    @property
    def card_token(self):
        if 'card_token' in self.response:
            return self.response['card_token']
