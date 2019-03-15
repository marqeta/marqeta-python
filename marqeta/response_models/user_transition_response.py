from datetime import datetime, date
import json

class UserTransitionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'status' : self.status,
           'reason_code' : self.reason_code,
           'reason' : self.reason,
           'channel' : self.channel,
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'user_token' : self.user_token,
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
    def status(self):
        if 'status' in self.json_response:
            return self.json_response['status']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def reason(self):
        if 'reason' in self.json_response:
            return self.json_response['reason']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    def __repr__(self):
         return '<Marqeta.response_models.user_transition_response.UserTransitionResponse>'