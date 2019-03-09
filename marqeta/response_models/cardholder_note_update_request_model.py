from datetime import datetime

class CardholderNoteUpdateRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def description(self):
        if 'description' in self.json_response:
            return self.json_response['description']

