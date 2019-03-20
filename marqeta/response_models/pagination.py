from datetime import datetime, date
import json

class Pagination(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def count(self):
        if 'count' in self.json_response:
            return self.json_response['count']

    @property
    def start_index(self):
        if 'start_index' in self.json_response:
            return self.json_response['start_index']

    @property
    def end_index(self):
        if 'end_index' in self.json_response:
            return self.json_response['end_index']

    @property
    def is_more(self):
        if 'is_more' in self.json_response:
            return self.json_response['is_more']

    @property
    def data(self):
        if 'data' in self.json_response:
            return self.json_response['data']

    def __repr__(self):
         return '<Marqeta.response_models.pagination.Pagination>'