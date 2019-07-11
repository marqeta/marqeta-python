from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class KycQuestion(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def key(self):
        return self.json_response.get('key', None)


    @property
    def question(self):
        return self.json_response.get('question', None)


    @property
    def answers(self):
        return self.json_response.get('answers', None)

    def __repr__(self):
         return '<Marqeta.response_models.kyc_question.KycQuestion>' + self.__str__()
