from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class TokenUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def exp_date(self):
        return self.json_response.get('exp_date', None)


    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def is_default_account(self):
        return self.json_response.get('is_default_account', None)

    def __repr__(self):
         return '<Marqeta.response_models.token_update_request.TokenUpdateRequest>' + self.__str__()
