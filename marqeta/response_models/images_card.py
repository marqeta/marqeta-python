from datetime import datetime, date
import json

class ImagesCard(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def thermal_color(self):
        if 'thermal_color' in self.json_response:
            return self.json_response['thermal_color']

    def __repr__(self):
         return '<Marqeta.response_models.images_card.ImagesCard>'