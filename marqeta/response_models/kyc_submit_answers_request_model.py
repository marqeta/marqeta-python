from datetime import datetime, date
from marqeta.response_models.kyc_answer import KycAnswer
import json


class KycSubmitAnswersRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def answers(self):
        if 'answers' in self.json_response:
            return [KycAnswer(val) for val in self.json_response['answers']]

    def __repr__(self):
        return '<Marqeta.response_models.kyc_submit_answers_request_model.KycSubmitAnswersRequestModel>'
