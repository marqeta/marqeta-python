from datetime import datetime, date
import json


class TransactionOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def additional_data(self):
        return self.json_response.get('additional_data', None)

    @property
    def database_transaction_timeout(self):
        return self.json_response.get('database_transaction_timeout', None)

    @property
    def pre_auth_time_limit(self):
        return self.json_response.get('pre_auth_time_limit', None)

    @property
    def send_expiration_date(self):
        return self.json_response.get('send_expiration_date', None)

    @property
    def send_track_data(self):
        return self.json_response.get('send_track_data', None)

    @property
    def card_expiration_date_yymm(self):
        return self.json_response.get('card_expiration_date_yymm', None)

    def __repr__(self):
        return '<Marqeta.response_models.transaction_options.TransactionOptions>'
