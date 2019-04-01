from datetime import datetime, date
import json


class MsaOrderRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def campaign_token(self):
        return self.json_response.get('campaign_token', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def currency_code(self):
        return self.json_response.get('currency_code', None)

    @property
    def purchase_amount(self):
        return self.json_response.get('purchase_amount', None)

    @property
    def reward_amount(self):
        return self.json_response.get('reward_amount', None)

    @property
    def reward_trigger_amount(self):
        return self.json_response.get('reward_trigger_amount', None)

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
            return datetime.strptime(self.json_response['start_date'], '%Y-%m-%d').date()

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return datetime.strptime(self.json_response['end_date'], '%Y-%m-%d').date()

    @property
    def funding_source_token(self):
        return self.json_response.get('funding_source_token', None)

    @property
    def funding_source_address_token(self):
        return self.json_response.get('funding_source_address_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.msa_order_request.MsaOrderRequest>'
