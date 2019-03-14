from datetime import datetime, date
import json

class KycQuestion(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'key' : self.key,
           'question' : self.question,
           'answers' : self.answers,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def key(self):
        if 'key' in self.json_response:
            return self.json_response['key']

    @property
    def question(self):
        if 'question' in self.json_response:
            return self.json_response['question']

    @property
    def answers(self):
        if 'answers' in self.json_response:
            return self.json_response['answers']

    def __repr__(self):
         return '<Marqeta.response_models.kyc_question.KycQuestion>'