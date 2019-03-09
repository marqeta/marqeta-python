from datetime import datetime

class SpendControlAssociation(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def card_product_token(self):
        if 'card_product_token' in self.json_response:
            return self.json_response['card_product_token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

