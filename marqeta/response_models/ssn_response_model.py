"""SSN Response Model with Ssn Properties!!!"""

class SsnResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

