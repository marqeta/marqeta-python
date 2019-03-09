from datetime import datetime

class KycAnswer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def answer(self):
        if 'answer' in self.json_response:
            return self.json_response['answer']

    @property
    def key(self):
        if 'key' in self.json_response:
            return self.json_response['key']

