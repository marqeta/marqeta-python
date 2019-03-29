from datetime import datetime, date
import json


class Transit(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction_type(self):
        return self.json_response.get('transaction_type', None)

    @property
    def transportation_mode(self):
        return self.json_response.get('transportation_mode', None)

    def __repr__(self):
        return '<Marqeta.response_models.transit.Transit>'
