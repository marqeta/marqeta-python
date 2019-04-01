from datetime import datetime, date
import json


class EchoPingResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def success(self):
        return self.json_response.get('success', None)

    @property
    def id(self):
        return self.json_response.get('id', None)

    @property
    def payload(self):
        return self.json_response.get('payload', None)

    def __repr__(self):
        return '<Marqeta.response_models.echo_ping_response.EchoPingResponse>' + self.__str__()
