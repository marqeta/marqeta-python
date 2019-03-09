from datetime import datetime

class PushToCardRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def address_1(self):
        if 'address_1' in self.json_response:
            return self.json_response['address_1']

    @property
    def address_2(self):
        if 'address_2' in self.json_response:
            return self.json_response['address_2']

    @property
    def city(self):
        if 'city' in self.json_response:
            return self.json_response['city']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def country(self):
        if 'country' in self.json_response:
            return self.json_response['country']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def name_on_card(self):
        if 'name_on_card' in self.json_response:
            return self.json_response['name_on_card']

    @property
    def pan(self):
        if 'pan' in self.json_response:
            return self.json_response['pan']

    @property
    def cvv(self):
        if 'cvv' in self.json_response:
            return self.json_response['cvv']

    @property
    def exp_date(self):
        if 'exp_date' in self.json_response:
            return self.json_response['exp_date']

