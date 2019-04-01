from datetime import datetime, date
import json


class BulkRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user_tokens(self):
        return self.json_response.get('user_tokens', None)

    @property
    def business_tokens(self):
        return self.json_response.get('business_tokens', None)

    @property
    def card_tokens(self):
        return self.json_response.get('card_tokens', None)

    @property
    def kyc_tokens(self):
        return self.json_response.get('kyc_tokens', None)

    @property
    def dda_tokens(self):
        return self.json_response.get('dda_tokens', None)

    def __repr__(self):
        return '<Marqeta.response_models.bulk_request_model.BulkRequestModel>' + self.__str__()
