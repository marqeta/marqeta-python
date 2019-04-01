from datetime import datetime, date
import json


class Network(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def original_amount(self):
        return self.json_response.get('original_amount', None)

    @property
    def conversion_rate(self):
        return self.json_response.get('conversion_rate', None)

    @property
    def original_currency_code(self):
        return self.json_response.get('original_currency_code', None)

    def __repr__(self):
        return '<Marqeta.response_models.network.Network>' + self.__str__()
