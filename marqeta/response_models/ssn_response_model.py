"""SSN Response Model with Ssn Properties!!!"""


class SsnResponse(object):

    def __init__(self, response):
        self.response = response

    @property
    def ssn(self):
        if 'ssn' in self.response:
            return self.response['ssn']
