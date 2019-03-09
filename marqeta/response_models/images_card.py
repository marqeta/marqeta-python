from datetime import datetime

class ImagesCard(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def thermal_color(self):
        if 'thermal_color' in self.json_response:
            return self.json_response['thermal_color']

