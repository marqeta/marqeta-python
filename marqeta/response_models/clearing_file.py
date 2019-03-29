from datetime import datetime, date
import json


class ClearingFile(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network(self):
        return self.json_response.get('network', None)

    @property
    def file(self):
        return self.json_response.get('file', None)

    def __repr__(self):
        return '<Marqeta.response_models.clearing_file.ClearingFile>'
