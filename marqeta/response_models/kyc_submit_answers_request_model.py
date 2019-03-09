from datetime import datetime
from marqeta.response_models.kyc_answer import KycAnswer

class KycSubmitAnswersRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def answers(self):
        if 'answers' in self.json_response:
            return [KycAnswer(val) for val in self.json_response['answers']]

