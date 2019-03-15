from datetime import datetime, date
import json

class PushToCardDisbursementResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'token' : self.token,
           'currency_code' : self.currency_code,
           'amount' : self.amount,
           'payment_instrument_token' : self.payment_instrument_token,
           'tags' : self.tags,
           'memo' : self.memo,
         }
        return json.dumps(dict, default=self.json_serial)

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
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def payment_instrument_token(self):
        if 'payment_instrument_token' in self.json_response:
            return self.json_response['payment_instrument_token']

    @property
    def tags(self):
        if 'tags' in self.json_response:
            return self.json_response['tags']

    @property
    def memo(self):
        if 'memo' in self.json_response:
            return self.json_response['memo']

    def __repr__(self):
         return '<Marqeta.response_models.push_to_card_disbursement_response.PushToCardDisbursementResponse>'