from datetime import datetime, date
import json


class PanRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pan(self):
        return self.json_response.get('pan', None)

    @property
    def cvv_number(self):
        return self.json_response.get('cvv_number', None)

    @property
    def expiration(self):
        return self.json_response.get('expiration', None)

    def __repr__(self):
        return '<Marqeta.response_models.pan_request.PanRequest>' + self.__str__()
