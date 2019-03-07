"""UserResource class lists all the user properties for the /user endpoint"""
from datetime import datetime


class CardProductResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def name(self):
        if 'name' in self.response:
            return self.response['name']

    @property
    def active(self):
        if 'active' in self.response:
            return self.response['active']

    @property
    def start_date(self):
        if 'start_date' in self.response:
            return datetime.strptime(self.response['start_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_date(self):
        if 'end_date' in self.response:
            return datetime.strptime(self.response['end_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def config(self):
        if 'config' in self.response:
            return self.response['config']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')
