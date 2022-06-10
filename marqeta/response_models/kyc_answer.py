from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class KycAnswer(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def answer(self):
        return self.json_response.get("answer", None)

    @property
    def key(self):
        return self.json_response.get("key", None)

    def __repr__(self):
        return "<Marqeta.response_models.kyc_answer.KycAnswer>" + self.__str__()
