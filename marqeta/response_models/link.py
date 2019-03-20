from datetime import datetime, date
import json

class Link(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.link.Link>'