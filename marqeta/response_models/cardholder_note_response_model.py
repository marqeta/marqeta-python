"""Card Holder Notes Model with Notes Properties!!!"""

from datetime import datetime


class CardHolderNotesResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def description(self):
        if 'description' in self.response:
            return self.response['description']

    @property
    def created_by(self):
        if 'created_by' in self.response:
            return self.response['created_by']

    @property
    def created_by_user_role(self):
        if 'created_by_user_role' in self.response:
            return self.response['created_by_user_role']

    @property
    def private(self):
        if 'private' in self.response:
            return self.response['private']

    @property
    def created_time(self):
        if 'created_time' in self.response:
            return datetime.strptime(self.response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.response:
            return datetime.strptime(self.response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')
