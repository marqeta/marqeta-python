from datetime import datetime

class ImagesCarrier(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def message_1(self):
        if 'message_1' in self.json_response:
            return self.json_response['message_1']

