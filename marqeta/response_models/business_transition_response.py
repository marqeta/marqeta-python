from datetime import datetime, date
import json


class BusinessTransitionResponse(object):

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
    def status(self):
        return self.json_response.get('status', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def reason(self):
        return self.json_response.get('reason', None)

    @property
    def channel(self):
        return self.json_response.get('channel', None)

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.business_transition_response.BusinessTransitionResponse>' + self.__str__()
