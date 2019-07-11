from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class AdviceRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def message(self):
        return self.json_response.get('message', None)


    @property
    def network(self):
        return self.json_response.get('network', None)


    def __repr__(self):
         return '<Marqeta.response_models.advice_request_model.AdviceRequestModel>' + self.__str__()
