from datetime import datetime

class Pagination(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

