from datetime import datetime, date
import json

class MerchantScope(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'mid' : self.mid,
           'mcc' : self.mcc,
           'mcc_group' : self.mcc_group,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def mcc(self):
        if 'mcc' in self.json_response:
            return self.json_response['mcc']

    @property
    def mcc_group(self):
        if 'mcc_group' in self.json_response:
            return self.json_response['mcc_group']

    def __repr__(self):
         return '<Marqeta.response_models.merchant_scope.MerchantScope>'