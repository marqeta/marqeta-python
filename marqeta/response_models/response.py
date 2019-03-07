from datetime import datetime


class Response(object):

    def __init__(self, response):
        self.response = response

    @property
    def code(self):
        if 'code' in self.response:
            return self.response['code']

    @property
    def memo(self):
        if 'memo' in self.response:
            return self.response['memo']
