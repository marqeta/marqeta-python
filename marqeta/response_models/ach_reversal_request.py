from datetime import datetime

class AchReversalRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

