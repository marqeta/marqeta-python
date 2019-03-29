from datetime import datetime, date
from marqeta.response_models.fee_detail import FeeDetail
import json


class FeeTransferResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def tags(self):

        return self.json_response.get('tags', None)

    @property
    def fees(self):

        if 'fees' in self.json_response:
            return [FeeDetail(val) for val in self.json_response['fees']]

    @property
    def token(self):

        return self.json_response.get('token', None)

    @property
    def user_token(self):

        return self.json_response.get('user_token', None)

    @property
    def business_token(self):

        return self.json_response.get('business_token', None)

    @property
    def created_time(self):

        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.fee_transfer_response.FeeTransferResponse>'
