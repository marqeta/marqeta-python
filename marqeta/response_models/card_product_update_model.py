from datetime import datetime
from marqeta.response_models.card_product_config import CardProductConfig

class CardProductUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
            return self.json_response['start_date']

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return self.json_response['end_date']

    @property
    def config(self):
        if 'config' in self.json_response:
            return CardProductConfig(self.json_response['config'])

