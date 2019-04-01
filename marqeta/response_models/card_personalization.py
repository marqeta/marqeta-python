from datetime import datetime, date
from marqeta.response_models.text import Text
from marqeta.response_models.images import Images
from marqeta.response_models.carrier import Carrier
import json


class CardPersonalization(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def text(self):
        if 'text' in self.json_response:
            return Text(self.json_response['text'])

    @property
    def images(self):
        if 'images' in self.json_response:
            return Images(self.json_response['images'])

    @property
    def carrier(self):
        if 'carrier' in self.json_response:
            return Carrier(self.json_response['carrier'])

    def __repr__(self):
        return '<Marqeta.response_models.card_personalization.CardPersonalization>'
