from datetime import datetime

class KycQuestion(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

