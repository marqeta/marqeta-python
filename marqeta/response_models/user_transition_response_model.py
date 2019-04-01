"""Authentication Model with Authentication Properties!!!"""
from datetime import datetime


class UserTransitionResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def token(self):
        if 'token' in self.response:
            return self.response['token']

    @property
    def status(self):
        if 'status' in self.response:
            return self.response['status']

    @property
    def reason_code(self):
        if 'reason_code' in self.response:
            return self.response['reason_code']

    @property
    def reason(self):
        if 'reason' in self.response:
            return self.response['reason']

    @property
    def channel(self):
        if 'channel' in self.response:
            return self.response['channel']

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

    def __repr__(self):
        return '<Marqeta.response_models.user_validation_request.UserTransitionResponse>' + self.__str__()
