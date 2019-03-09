from datetime import datetime

class Link(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def rel(self):
        if 'rel' in self.json_response:
            return self.json_response['rel']

    @property
    def method(self):
        if 'method' in self.json_response:
            return self.json_response['method']

    @property
    def href(self):
        if 'href' in self.json_response:
            return self.json_response['href']

