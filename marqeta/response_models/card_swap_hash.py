from datetime import datetime

class CardSwapHash(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def previous_card_token(self):
        if 'previous_card_token' in self.json_response:
            return self.json_response['previous_card_token']

    @property
    def new_card_token(self):
        if 'new_card_token' in self.json_response:
            return self.json_response['new_card_token']

