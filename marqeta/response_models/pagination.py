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
        return self.json_response.get('count', None)

    @property
    def start_index(self):
        return self.json_response.get('start_index', None)

    @property
    def end_index(self):
        return self.json_response.get('end_index', None)

    @property
    def is_more(self):
        return self.json_response.get('is_more', None)

    @property
    def data(self):
        return self.json_response.get('data', None)

    def __repr__(self):
        return '<Marqeta.response_models.pagination.Pagination>'
