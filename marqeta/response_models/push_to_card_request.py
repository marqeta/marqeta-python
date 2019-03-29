from datetime import datetime, date
import json


class PushToCardRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def address_1(self):
        return self.json_response.get('address_1', None)

    @property
    def address_2(self):
        return self.json_response.get('address_2', None)

    @property
    def city(self):
        return self.json_response.get('city', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def zip(self):
        return self.json_response.get('zip', None)

    @property
    def country(self):
        return self.json_response.get('country', None)

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def name_on_card(self):
        return self.json_response.get('name_on_card', None)

    @property
    def pan(self):
        return self.json_response.get('pan', None)

    @property
    def cvv(self):
        return self.json_response.get('cvv', None)

    @property
    def exp_date(self):
        return self.json_response.get('exp_date', None)

    def __repr__(self):
        return '<Marqeta.response_models.push_to_card_request.PushToCardRequest>'
