from datetime import datetime
from marqeta.response_models.images_card import ImagesCard
from marqeta.response_models.images_carrier import ImagesCarrier
from marqeta.response_models.images_signature import ImagesSignature
from marqeta.response_models.images_carrier_return_window import ImagesCarrierReturnWindow

class Images(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def card(self):
        if 'card' in self.json_response:
            return ImagesCard(self.json_response['card'])

    @property
    def carrier(self):
        if 'carrier' in self.json_response:
            return ImagesCarrier(self.json_response['carrier'])

    @property
    def signature(self):
        if 'signature' in self.json_response:
            return ImagesSignature(self.json_response['signature'])

    @property
    def carrier_return_window(self):
        if 'carrier_return_window' in self.json_response:
            return ImagesCarrierReturnWindow(self.json_response['carrier_return_window'])

