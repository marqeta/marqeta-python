from datetime import datetime, date
import json

class CardSwapHash(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def previous_card_token(self):
        if 'previous_card_token' in self.json_response:
            return self.json_response['previous_card_token']

    @property
    def new_card_token(self):
        if 'new_card_token' in self.json_response:
            return self.json_response['new_card_token']

    def __repr__(self):
         return '<Marqeta.response_models.card_swap_hash.CardSwapHash>'