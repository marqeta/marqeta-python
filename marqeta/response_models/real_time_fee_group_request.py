from datetime import datetime, date
import json

class RealTimeFeeGroupRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'active' : self.active,
           'fee_tokens' : self.fee_tokens,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def fee_tokens(self):
        if 'fee_tokens' in self.json_response:
            return self.json_response['fee_tokens']

    def __repr__(self):
         return '<Marqeta.response_models.real_time_fee_group_request.RealTimeFeeGroupRequest>'