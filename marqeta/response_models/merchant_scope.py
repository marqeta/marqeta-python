from datetime import datetime, date
import json


class MerchantScope(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def mid(self):
        return self.json_response.get('mid', None)

    @property
    def mcc(self):
        return self.json_response.get('mcc', None)

    @property
    def mcc_group(self):
        return self.json_response.get('mcc_group', None)

    def __repr__(self):
        return '<Marqeta.response_models.merchant_scope.MerchantScope>'
