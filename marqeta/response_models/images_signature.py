from datetime import datetime

class ImagesSignature(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

