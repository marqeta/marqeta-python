from datetime import datetime

class CardholderAuthenticationData(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def electronic_commerce_indicator(self):
        if 'electronic_commerce_indicator' in self.json_response:
            return self.json_response['electronic_commerce_indicator']

    @property
    def verification_result(self):
        if 'verification_result' in self.json_response:
            return self.json_response['verification_result']

    @property
    def verification_value_created_by(self):
        if 'verification_value_created_by' in self.json_response:
            return self.json_response['verification_value_created_by']

