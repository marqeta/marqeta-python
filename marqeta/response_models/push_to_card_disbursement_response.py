from datetime import datetime, date
import json


class PushToCardDisbursementResponse(object):

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
    def token(self):

        return self.json_response.get('token', None)

    @property
    def currency_code(self):

        return self.json_response.get('currency_code', None)

    @property
    def amount(self):

        return self.json_response.get('amount', None)

    @property
    def payment_instrument_token(self):

        return self.json_response.get('payment_instrument_token', None)

    @property
    def tags(self):

        return self.json_response.get('tags', None)

    @property
    def memo(self):

        return self.json_response.get('memo', None)

    def __repr__(self):
        return '<Marqeta.response_models.push_to_card_disbursement_response.PushToCardDisbursementResponse>'
