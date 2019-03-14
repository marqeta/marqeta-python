from datetime import datetime, date
import json

class ImagesCarrier(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'message_1' : self.message_1,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def message_1(self):
        if 'message_1' in self.json_response:
            return self.json_response['message_1']

    def __repr__(self):
         return '<Marqeta.response_models.images_carrier.ImagesCarrier>'