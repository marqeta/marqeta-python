from datetime import datetime
from marqeta.response_models.cardholder_balance import CardholderBalance
from marqeta.response_models.link import Link

class CardholderBalances(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def gpa(self):
        if 'gpa' in self.json_response:
            return CardholderBalance(self.json_response['gpa'])

    @property
    def links(self):
        if 'links' in self.json_response:
            return [Link(val) for val in self.json_response['links']]

