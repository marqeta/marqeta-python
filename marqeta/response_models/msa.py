from datetime import datetime, date
import json


class Msa(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def campaign_token(self):
        return self.json_response.get('campaign_token', None)

    @property
    def trigger_amount(self):
        return self.json_response.get('trigger_amount', None)

    @property
    def reload_amount(self):
        return self.json_response.get('reload_amount', None)

    def __repr__(self):
        return '<Marqeta.response_models.msa.Msa>'
