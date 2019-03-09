from datetime import datetime

class DigitalWalletApplePayProvisionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def encrypted_pass_data(self):
        if 'encrypted_pass_data' in self.json_response:
            return self.json_response['encrypted_pass_data']

    @property
    def activation_data(self):
        if 'activation_data' in self.json_response:
            return self.json_response['activation_data']

    @property
    def ephemeral_public_key(self):
        if 'ephemeral_public_key' in self.json_response:
            return self.json_response['ephemeral_public_key']

