from datetime import datetime
from marqeta.response_models.shipping import Shipping
from marqeta.response_models.card_personalization import CardPersonalization

class Fulfillment(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def shipping(self):
        if 'shipping' in self.json_response:
            return Shipping(self.json_response['shipping'])

    @property
    def card_personalization(self):
        if 'card_personalization' in self.json_response:
            return CardPersonalization(self.json_response['card_personalization'])

