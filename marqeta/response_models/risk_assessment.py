from datetime import datetime

class RiskAssessment(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def score(self):
        if 'score' in self.json_response:
            return self.json_response['score']

    @property
    def version(self):
        if 'version' in self.json_response:
            return self.json_response['version']

