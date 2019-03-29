from datetime import datetime, date
import json


class CardInventoryRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def package_id(self):
        return self.json_response.get('package_id', None)

    @property
    def starting_inventory(self):
        return self.json_response.get('starting_inventory', None)

    def __repr__(self):
        return '<Marqeta.response_models.card_inventory_request.CardInventoryRequest>'
