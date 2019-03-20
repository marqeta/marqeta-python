from datetime import datetime, date
import json

class UserCardHolderSearchModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

    @property
    def dda(self):
        if 'dda' in self.json_response:
            return self.json_response['dda']

    @property
    def first_name(self):
        if 'first_name' in self.json_response:
            return self.json_response['first_name']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

    def __repr__(self):
         return '<Marqeta.response_models.user_card_holder_search_model.UserCardHolderSearchModel>'