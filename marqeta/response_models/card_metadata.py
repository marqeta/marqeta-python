from datetime import datetime, date
import json

class CardMetadata(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'metadata' : self.metadata,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    def __repr__(self):
         return '<Marqeta.response_models.card_metadata.CardMetadata>'