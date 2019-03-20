from datetime import datetime, date
import json

class PushToCardResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

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
    def last_four(self):
        if 'last_four' in self.json_response:
            return self.json_response['last_four']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def fast_fund_transfer_eligible(self):
        if 'fast_fund_transfer_eligible' in self.json_response:
            return self.json_response['fast_fund_transfer_eligible']

    @property
    def gambling_fund_transfer_eligible(self):
        if 'gambling_fund_transfer_eligible' in self.json_response:
            return self.json_response['gambling_fund_transfer_eligible']

    @property
    def name_on_card(self):
        if 'name_on_card' in self.json_response:
            return self.json_response['name_on_card']

    @property
    def last_name(self):
        if 'last_name' in self.json_response:
            return self.json_response['last_name']

    @property
    def exp_date(self):
        if 'exp_date' in self.json_response:
            return self.json_response['exp_date']

    def __repr__(self):
         return '<Marqeta.response_models.push_to_card_response.PushToCardResponse>'